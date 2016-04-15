from PyQt4.uic.uiparser import QtGui

import os
import os.path
from cmath import phase
from itertools import (takewhile,repeat)
import numpy as np
import pandas as pd

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from numpy import linspace
from numpy.ma import angle

import file_dialog_gui
import plot_dialog_gui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib import rcParams
rcParams['font.size'] = 9
rcParams['agg.path.chunksize'] = 10000

class mpl_widget(Canvas):

    def __init__(self,
                 parent=None,
                 title='',
                 xlabel='',
                 ylabel='',
                 xlim=None,
                 ylim=None,
                 xscale='linear',
                 yscale='linear',
                 width=10,
                 height=5,
                 dpi=100,
                 dimension = '111',
                 bgcolor  = 'k',
                 hold=True):

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(dimension)
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.bgcolor = bgcolor

        if xscale is not None:
            self.axes.set_xscale(xscale)
        if yscale is not None:
            self.axes.set_yscale(yscale)
        if xlim is not None:
            self.axes.set_xlim(*xlim)
        if ylim is not None:
            self.axes.set_ylim(*ylim)
        self.axes.hold(hold)

        Canvas.__init__(self, self.figure)
        self.setParent(parent)

        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(50, 50)


#=================file dialog ================================
class file_dialog(QDialog,file_dialog_gui.Ui_Dialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)

        #==================================================
        #set fixed size for the reader
        self.setFixedSize(self.size())

        #=============variables to keep for gui============
        self.val_file_name       = ""
        self.val_row_start       = 0
        self.val_row_stop        = 0
        self.val_num_column      = 0
        self.val_num_column_skip = 0;
        self.val_data_type       = "none"

        #=======signal slot connection=====================
        self.b_file.clicked.connect(self.click_open_file)
        self.b_done.clicked.connect(self.click_done)

    def click_open_file(self):
        fn = QFileDialog.getOpenFileName(self, "Open File...", ".", "Data File (*.dat *.txt *.log);;All Files (*)")
        if(os.path.isfile(fn) and  os.access(fn,os.R_OK)):
            self.val_file_name = fn
            self.e_file_edit.setText(fn)
        else:
            quit_msg = "File cannot be opend, it does not exisit or its not readable"
            reply = QMessageBox.critical(self, 'Open File First',
                     quit_msg, QMessageBox.Close)

    def click_done(self):
        self.val_row_start       = self.e_row_start.text()
        self.val_row_stop        = self.e_row_stop.text()
        self.val_num_column      = self.e_num_column.text()
        self.val_num_column_skip = self.num_column_skip.text()
        if (self.b_rb_real.isChecked()):
            self.val_data_type       = "real_type"
        elif(self.b_rb_complex.isChecked()):
            self.val_data_type       = "complex_type"
        else:
            self.val_data_type       = "none"
        self.hide()


#=====================plot dialog=================================
class plot_dialog(QDialog,plot_dialog_gui.Ui_Dialog):
    def __init__(self,parent=None,reader=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        #set fixed size for the plot dialog
        self.setFixedSize(self.size())
        #hide the progress bar in the begning
        self.p_progress_bar.hide()
        for i in range(0,int(reader.val_num_column)):
            self.b_column_choose.addItem(str(i))
        #=============variables to keep for gui============
        self.val_plot_dimention     = 111
        self.val_subplot            = 111
        self.val_color              = 'b'
        self.val_sample_freq        = 0
        self.val_num_fft_points     = 0
        self.reader                 = reader
        self.num_lines              = 0
        self.plot_widget            = parent
        self.val_column_choose      = int(self.b_column_choose.currentText())
        self.val_average_N          = 0
        self.val_row_start          = int(self.reader.val_row_start)
        self.val_row_stop           = int(self.reader.val_row_stop)
        self.val_data_type          = "REAL" if self.reader.b_rb_real.isChecked() else "COMPLEX" 

        self.b_plot_real.clicked.connect(self.click_plot_real)
        self.b_plot_complex.clicked.connect(self.click_plot_complex)
        self.b_plot_fft.clicked.connect(self.click_plot_fft)
        self.b_done.clicked.connect(self.click_done)
        self.b_clean.clicked.connect(self.click_clean)
        self.b_slider.valueChanged.connect(self.click_slider)

        #=======find the number of lines in file===========
        self.rawbigcount()
        #=== create the array with the number of lines
        self.plot_data         = np.empty((int(self.num_lines),int(self.reader.val_num_column)), dtype='float')


    def click_plot_real(self):
        self.get_configs()
        self.plot_data         = np.empty((int(self.num_lines),int(self.reader.val_num_column)), dtype='float')
        self.p_progress_bar.setMaximum(self.num_lines)
        self.p_progress_bar.show()
        self.read_file()
        y = np.arange(0,len(self.plot_data))
        x = self.plot_data[::,self.val_column_choose]
        if (self.b_cb_hold.isChecked()):
            self.plot_widget.canvas.axes.hold(True)
        else:
            self.plot_widget.canvas.axes.hold(False)
        self.plot_widget.canvas.axes = self.plot_widget.canvas.figure.add_subplot(self.val_subplot)
        self.plot_widget.canvas.axes.set_axis_bgcolor(str( self.plot_widget.canvas.bgcolor))
        self.plot_widget.canvas.axes.plot(y,x, color=str(self.val_color))
        self.plot_widget.canvas.draw()
        self.hide()

    def click_plot_complex(self):
        plot_complex_data = np.empty((int(self.num_lines)), dtype='complex64')
        r_data = np.empty((int(self.num_lines)), dtype='complex64')
        phi_data = np.empty((int(self.num_lines)), dtype='complex64')
        self.get_configs()
        self.p_progress_bar.setMaximum(self.num_lines)
        self.p_progress_bar.show()
        self.read_file()
        y = self.plot_data[::,1]
        x = self.plot_data[::,0]
        plot_complex_data =  x + 1j*y;
        r_data    = abs(plot_complex_data)
        phi_data  = angle(plot_complex_data)
        if (self.b_cb_hold.isChecked()):
            self.plot_widget.canvas.axes.hold(True)
        else:
            self.plot_widget.canvas.axes.hold(False)
        self.plot_widget.canvas.axes = self.plot_widget.canvas.figure.add_subplot(self.val_subplot,projection='polar')
        self.plot_widget.canvas.axes.set_axis_bgcolor(str( self.plot_widget.canvas.bgcolor))
        self.plot_widget.canvas.axes.plot(phi_data,r_data, color=str(self.val_color))
        self.plot_widget.canvas.draw()
        self.hide()

    def click_plot_fft(self):
        self.do_fft()

    def click_done(self):
        self.hide()

    def click_clean(self):
        self.plot_widget.canvas.figure.clear()
        self.plot_widget.canvas.axes = self.plot_widget.canvas.figure.add_subplot(self.val_plot_dimention)
        self.plot_widget.canvas.draw()
        
    def click_slider(self):
        self.l_average_window.setText(("Moving Average =%0s" % (self.b_slider.value())))

    def rawbigcount(self):
        f = open(self.reader.val_file_name, 'r')
        bufgen = takewhile(lambda x: x, (f.read(1024*1024) for _ in repeat(None)))
        self.num_lines = sum( buf.count(b'\n') for buf in bufgen if buf )
        self.num_lines = self.num_lines-self.val_row_start

    def get_configs(self):
        self.rawbigcount()
        self.plot_data         = np.empty((int(self.num_lines),int(self.reader.val_num_column)), dtype='float')

        if (self.val_plot_dimention !=  self.e_dimension.text()):
            self.val_plot_dimention     = self.e_dimension.text()
            self.plot_widget.canvas.figure.clear()
            self.plot_widget.canvas.axes = self.plot_widget.canvas.figure.add_subplot(self.val_plot_dimention)
            self.plot_widget.canvas.axes.set_axis_bgcolor(str( self.plot_widget.canvas.bgcolor))
            
        self.val_subplot            = self.e_subplot.text()
        self.val_color              = self.e_color.text()
        self.val_sample_freq        = self.e_sample_freq.text()
        self.val_num_fft_points     = self.e_num_fft_points.text()
        self.val_column_choose      = int(self.b_column_choose.currentText())
        self.val_average_N          = int(self.b_slider.value())
        self.val_row_start          = int(self.reader.val_row_start)
        self.val_row_stop           = int(self.reader.val_row_stop)
        self.val_data_type          = "REAL" if self.reader.b_rb_real.isChecked() else "COMPLEX" 

    def read_file(self):
        cols  = 0
        rows   = 0
        line_count = 0;
        print(cols)
        print(rows)
        print(line_count)
        self.p_progress_bar.setValue(0)
        with open(self.reader.val_file_name, "r") as file:
            for line in file:
                #if (cols >= self.reader.val_row_start and (cols <= self.reader.val_row_stop or self.reader.val_row_stop == -1)):
                values = line.split()
                cols = 0
                if (line_count < self.val_row_start):
                    line_count+=1
                else:
                    for value in values:
                        if (int(self.reader.val_num_column) > cols):
                            self.plot_data[rows][cols] = value
                            cols = cols + 1
                    rows = rows + 1
                    self.p_progress_bar.setValue(rows)
                

    def running_mean(self,x, N):
        return pd.rolling_mean(x,N)
        #return pd.Series.rolling(x,N)

    def do_fft(self):
        plot_complex_data = np.empty((int(self.num_lines)), dtype='complex64')
        self.get_configs()
        fft_size = int(self.num_lines)
        self.p_progress_bar.setMaximum(self.num_lines)
        self.p_progress_bar.show()
        self.read_file()
        if (self.val_data_type == "COMPLEX"):
            y = self.plot_data[::,1]
            x = self.plot_data[::,0]
            t = range(0,len(x))
            plot_complex_data =  x + 1j*y;
        else:
            x = self.plot_data[::,0]
            t = range(0,len(x))
            plot_complex_data =  x + 1j*0;

        if (self.b_cb_hold.isChecked()):
            self.plot_widget.canvas.axes.hold(True)
        else:
            self.plot_widget.canvas.axes.hold(False)
        nfft_points = int(self.val_num_fft_points)
        if (nfft_points == 0):
            nfft_points = int(fft_size)

        fft_val = np.fft.fftshift(np.fft.fft(plot_complex_data,nfft_points))/nfft_points
        t= fVals= float(self.val_sample_freq) * np.arange(-0.5,0.5,1.0/(nfft_points))
        abs_fft = abs(fft_val)
        avg_fft_val = self.running_mean(abs_fft,self.val_average_N)
        self.plot_widget.canvas.axes = self.plot_widget.canvas.figure.add_subplot(self.val_subplot)
        self.plot_widget.canvas.axes.set_facecolor(str( self.plot_widget.canvas.bgcolor))
        self.plot_widget.canvas.axes.plot(t,avg_fft_val, color=str(self.val_color))
        self.plot_widget.canvas.draw()
        self.hide()

class plot_widget(QWidget):

    def __init__(self,
                 parent=None,
                 title='',
                 xlabel='',
                 ylabel='',
                 width=10,
                 height=5,
                 dpi=100,
                 dimension = '111',
                 bgcolor   = '#262626'
                 ):
        QWidget.__init__(self,parent)
        self.canvas        = mpl_widget(
            self,
                 title      = title,
                 xlabel     = xlabel,
                 ylabel     = ylabel,
                 xlim       = None,
                 ylim       = None,
                 xscale     = 'linear',
                 yscale     = 'linear',
                 width      = int(width),
                 height     = int(height),
                 dpi        = int(dpi),
                 dimension  = dimension,
                 bgcolor    = bgcolor,
                 hold       = True)
        self.toolbar       = NavigationToolbar(self.canvas, None)
        self.v_layout      = QVBoxLayout()
        #============vairables to hold the dialog objects==========
        self.fd = None
        self.pd = None
        #self.canvas.axes.
        #==================toolbar gui components==========
        #reader button
        self.b_read_file   = QPushButton("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/imag/read_file_2.png"), QIcon.Normal, QIcon.On)
        self.b_read_file.setIcon(icon1)
        self.b_read_file.clicked.connect(self.b_read_file_clicked)
        self.b_read_file.setIconSize(QSize(48, 48));
        self.b_plot_data   = QPushButton("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/imag/plot.png"), QIcon.Normal, QIcon.On)
        self.b_plot_data.setIcon(icon1)
        self.b_plot_data.clicked.connect(self.b_plot_button_clicked)
        self.b_plot_data.setIconSize(QSize(48, 48));
        #==============add widgets to toolbar
        self.toolbar.addWidget(self.b_read_file)
        self.toolbar.addWidget(self.b_plot_data)
        #
        self.setMinimumSize(self.toolbar.size())
        self.setMinimumSize(self.canvas.size())
        self.v_layout.addWidget(self.toolbar)
        self.v_layout.addWidget(self.canvas)
        self.setLayout(self.v_layout)

    def b_read_file_clicked(self):
        if (self.fd == None):
            self.fd = file_dialog()
            self.fd.exec_()
        else:
            self.fd.show()
            self.fd.exec_()
            
    def b_plot_button_clicked(self):
        if (self.fd == None):
            quit_msg = "Please open the file first, its not possible to plot"
            reply = QMessageBox.critical(self, 'File First',
                     quit_msg, QMessageBox.Close)
        else:
            if (self.pd == None):
                self.pd = plot_dialog(self,self.fd)
                self.pd.exec_()
            else:
                self.pd.show()
                self.pd.exec_()
                



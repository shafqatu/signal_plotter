#!/usr/bin/env python

#App to visualize signals and their FFTs
#=================all the imports===============================
from PyQt4 import QtGui,QtCore
import sys
from resource_rc import *
import signal_plotter_gui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_widget import plot_widget,mpl_widget
import figure_dialog_gui
from numpy import linspace

#=====================dialog for figure options==========================
class figure_dialog(QtGui.QDialog,figure_dialog_gui.Ui_Dialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.val_plot_dimention     = '111'
        self.val_title              = ''
        self.val_xlabel             = ''
        self.val_ylabel             = ''
        self.val_width              = 10
        self.val_height             = 5
        self.val_dpi                = 75
        self.val_bg_color           = '#262626'

        self.b_done.clicked.connect(self.click_done);

    def click_done(self):
        self.val_plot_dimention = self.e_dimension.text()
        self.val_title          = self.e_title.text()
        self.val_xlabel         = self.e_xlabel.text()
        self.val_ylabel         = self.e_ylabel.text()
        self.val_height         = self.e_height.text()
        self.val_width          = self.e_wight.text()
        self.val_dpi            = self.e_dpi.text()
        self.val_bg_color       = self.e_bg_color.text()
        self.hide()

#============= class the connect the gui with code========================
class signal_plotter(QtGui.QMainWindow, signal_plotter_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(signal_plotter, self).__init__(parent)
        self.setupUi(self)

        # make a vertical container to hold widgets
        self.main_widget = self.centralwidget
        self.v_layout = QtGui.QVBoxLayout(self.main_widget)

        self.plot_list = list()

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark);
        self.scrollArea.setWidget(self.main_widget);
        self.setCentralWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.show()

        self.actionNew_Plot.triggered.connect(self.new_plot)
        self.actionExit.triggered.connect(QtGui.qApp.quit)
        self.actionSettings.triggered.connect(self.settings_func)

    def new_plot(self):
        fd = figure_dialog()
        fd.exec_()
        self.plot_list.append(plot_widget(self.main_widget,
                                          fd.val_title,
                                          fd.val_xlabel,
                                          fd.val_ylabel,
                                          fd.val_width,
                                          fd.val_height,
                                          fd.val_dpi,
                                          fd.val_plot_dimention,
                                          fd.val_bg_color
                                          ))
        self.plot_list[-1].setMinimumSize(self.plot_list[-1].size())
        self.v_layout.addWidget(self.plot_list[-1])

    def settings_func(self):
        print("Settings Apllied")
        print ("New File Opened")


#==============function to make the gui window and display it=============
def main():
    app = QtGui.QApplication(sys.argv)
    win = signal_plotter()
    win.show()
    app.exec_()

#=============call the main function=====================
if __name__ == '__main__':
    main()



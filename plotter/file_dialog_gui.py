# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\file_dialog_gui.ui'
#
# Created: Sat Apr 09 03:52:51 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(414, 392)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imag/open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 383, 374))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.b_rb_complex = QtGui.QRadioButton(self.gridLayoutWidget)
        self.b_rb_complex.setCheckable(True)
        self.b_rb_complex.setChecked(True)
        self.b_rb_complex.setObjectName(_fromUtf8("b_rb_complex"))
        self.gridLayout.addWidget(self.b_rb_complex, 4, 3, 1, 1)
        self.e_row_stop = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_row_stop.setObjectName(_fromUtf8("e_row_stop"))
        self.gridLayout.addWidget(self.e_row_stop, 2, 2, 1, 1)
        self.num_column_skip = QtGui.QLineEdit(self.gridLayoutWidget)
        self.num_column_skip.setObjectName(_fromUtf8("num_column_skip"))
        self.gridLayout.addWidget(self.num_column_skip, 4, 2, 1, 1)
        self.e_row_start = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_row_start.setObjectName(_fromUtf8("e_row_start"))
        self.gridLayout.addWidget(self.e_row_start, 1, 2, 1, 1)
        self.b_rb_real = QtGui.QRadioButton(self.gridLayoutWidget)
        self.b_rb_real.setChecked(False)
        self.b_rb_real.setObjectName(_fromUtf8("b_rb_real"))
        self.gridLayout.addWidget(self.b_rb_real, 3, 3, 1, 1)
        self.e_file_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_file_edit.setObjectName(_fromUtf8("e_file_edit"))
        self.gridLayout.addWidget(self.e_file_edit, 0, 2, 1, 2)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.e_num_column = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_num_column.setObjectName(_fromUtf8("e_num_column"))
        self.gridLayout.addWidget(self.e_num_column, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/imag/plot_icon.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.b_file = QtGui.QPushButton(self.gridLayoutWidget)
        self.b_file.setIcon(icon)
        self.b_file.setIconSize(QtCore.QSize(48, 48))
        self.b_file.setObjectName(_fromUtf8("b_file"))
        self.gridLayout.addWidget(self.b_file, 1, 3, 1, 1)
        self.b_done = QtGui.QPushButton(self.gridLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/imag/done.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_done.setIcon(icon1)
        self.b_done.setIconSize(QtCore.QSize(48, 48))
        self.b_done.setObjectName(_fromUtf8("b_done"))
        self.gridLayout.addWidget(self.b_done, 2, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Reader", None))
        self.label_4.setText(_translate("Dialog", "Num Columns", None))
        self.label.setText(_translate("Dialog", "Fille Name", None))
        self.b_rb_complex.setText(_translate("Dialog", "Complex", None))
        self.e_row_stop.setText(_translate("Dialog", "-1", None))
        self.num_column_skip.setText(_translate("Dialog", "-1", None))
        self.e_row_start.setText(_translate("Dialog", "1", None))
        self.b_rb_real.setText(_translate("Dialog", "Real", None))
        self.label_3.setText(_translate("Dialog", "Row Stop", None))
        self.label_5.setText(_translate("Dialog", "Skip Columns", None))
        self.e_num_column.setText(_translate("Dialog", "2", None))
        self.label_2.setText(_translate("Dialog", "Row Start", None))
        self.b_file.setText(_translate("Dialog", "Open File", None))
        self.b_done.setText(_translate("Dialog", "Done", None))

import resource_rc

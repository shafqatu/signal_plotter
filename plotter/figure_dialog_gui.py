# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\figure_dialog_gui.ui'
#
# Created: Sat Apr 09 03:35:31 2016
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
        Dialog.resize(271, 324)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 264, 281))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.e_title = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_title.setObjectName(_fromUtf8("e_title"))
        self.gridLayout.addWidget(self.e_title, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.e_dpi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_dpi.setObjectName(_fromUtf8("e_dpi"))
        self.gridLayout.addWidget(self.e_dpi, 6, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.e_xlabel = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_xlabel.setObjectName(_fromUtf8("e_xlabel"))
        self.gridLayout.addWidget(self.e_xlabel, 2, 2, 1, 1)
        self.e_ylabel = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_ylabel.setObjectName(_fromUtf8("e_ylabel"))
        self.gridLayout.addWidget(self.e_ylabel, 3, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.e_wight = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_wight.setObjectName(_fromUtf8("e_wight"))
        self.gridLayout.addWidget(self.e_wight, 5, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.e_dimension = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_dimension.setObjectName(_fromUtf8("e_dimension"))
        self.gridLayout.addWidget(self.e_dimension, 0, 2, 1, 1)
        self.e_height = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_height.setObjectName(_fromUtf8("e_height"))
        self.gridLayout.addWidget(self.e_height, 4, 2, 1, 1)
        self.e_bg_color = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_bg_color.setObjectName(_fromUtf8("e_bg_color"))
        self.gridLayout.addWidget(self.e_bg_color, 7, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.b_done = QtGui.QPushButton(Dialog)
        self.b_done.setGeometry(QtCore.QRect(110, 290, 41, 27))
        self.b_done.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imag/done.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_done.setIcon(icon)
        self.b_done.setIconSize(QtCore.QSize(32, 32))
        self.b_done.setDefault(False)
        self.b_done.setFlat(True)
        self.b_done.setObjectName(_fromUtf8("b_done"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_6.setText(_translate("Dialog", "Width", None))
        self.label_5.setText(_translate("Dialog", "Height", None))
        self.e_dpi.setText(_translate("Dialog", "120", None))
        self.label_2.setText(_translate("Dialog", "Title", None))
        self.label_7.setText(_translate("Dialog", "Dpi", None))
        self.label_4.setText(_translate("Dialog", "Ylabel", None))
        self.label.setText(_translate("Dialog", "Figure Dimensions:", None))
        self.e_wight.setText(_translate("Dialog", "10", None))
        self.label_3.setText(_translate("Dialog", "XLabel", None))
        self.e_dimension.setText(_translate("Dialog", "111", None))
        self.e_height.setText(_translate("Dialog", "8", None))
        self.e_bg_color.setText(_translate("Dialog", "#ffffff", None))
        self.label_8.setText(_translate("Dialog", "Bg Color", None))

import resource_rc

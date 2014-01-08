# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'option.ui'
#
# Created: Fri Apr 26 16:18:08 2013
#      by: PyQt4 UI code generator 4.10.1
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
        Dialog.resize(250, 150)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 100, 180, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 10, 64, 33))
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(2.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.05)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 45, 171, 41))
        self.label.setObjectName(_fromUtf8("label"))
        

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Timer", None))
        self.label.setText(_translate("Dialog", "Frequenza di lettura dati", None))
        
    
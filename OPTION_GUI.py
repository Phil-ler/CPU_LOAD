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
        Dialog.resize(277, 364)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 300, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 40, 64, 33))
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(2.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.05)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 40, 171, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 130, 231, 161))
        self.textEdit.setObjectName(_fromUtf8("txt_IP"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Impostazioni", None))
        self.label.setText(_translate("Dialog", "Frequenza di lettura dati", None))
        self.label_2.setText(_translate("Dialog", "Lista di IP preimpostati", None))

    
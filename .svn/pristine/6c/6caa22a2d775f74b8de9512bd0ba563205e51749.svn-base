# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitoraggio.ui'
#
# Created: Tue Aug 27 23:04:16 2013
#      by: PyQt4 UI code generator 4.10.3
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
        Dialog.resize(236, 383)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 340, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 150, 59, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 250, 59, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_status = QtGui.QLabel(Dialog)
        self.lbl_status.setGeometry(QtCore.QRect(10, 320, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_status.setFont(font)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 301))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioLetture = QtGui.QRadioButton(self.groupBox)
        self.radioLetture.setGeometry(QtCore.QRect(20, 30, 191, 20))
        self.radioLetture.setObjectName(_fromUtf8("radioLetture"))
        self.radioTime = QtGui.QRadioButton(self.groupBox)
        self.radioTime.setGeometry(QtCore.QRect(20, 110, 181, 20))
        self.radioTime.setObjectName(_fromUtf8("radioTime"))
        self.timeInizio = QtGui.QTimeEdit(self.groupBox)
        self.timeInizio.setGeometry(QtCore.QRect(40, 160, 118, 25))
        self.timeInizio.setTimeSpec(QtCore.Qt.UTC)
        self.timeInizio.setObjectName(_fromUtf8("timeInizio"))
        self.timeFine = QtGui.QTimeEdit(self.groupBox)
        self.timeFine.setGeometry(QtCore.QRect(40, 260, 118, 25))
        self.timeFine.setObjectName(_fromUtf8("timeFine"))
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(40, 60, 51, 25))
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(500)
        self.spinBox.setSingleStep(10)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.checkChiusura = QtGui.QCheckBox(self.groupBox)
        self.checkChiusura.setGeometry(QtCore.QRect(40, 200, 181, 20))
        self.checkChiusura.setObjectName(_fromUtf8("checkChiusura"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Inizio", None))
        self.label_2.setText(_translate("Dialog", "Fine", None))
        self.lbl_status.setText(_translate("Dialog", "Pronto", None))
        self.groupBox.setTitle(_translate("Dialog", "Tipo di Monitoraggio", None))
        self.radioLetture.setText(_translate("Dialog", "Monitoraggio per letture", None))
        self.radioTime.setText(_translate("Dialog", "Monitoraggio per tempo", None))
        self.timeInizio.setDisplayFormat(_translate("Dialog", "HH:mm:ss", None))
        self.timeFine.setDisplayFormat(_translate("Dialog", "HH:mm:ss", None))
        self.checkChiusura.setText(_translate("Dialog", "Dopo chiusura ", None))


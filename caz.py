# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPU_GUI.ui'
#
# Created: Sat Mar 23 12:10:19 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_frmHost(object):
    def setupUi(self, frmHost):
        frmHost.setObjectName(_fromUtf8("frmHost"))
        frmHost.resize(470, 367)
        self.verticalLayout = QtGui.QVBoxLayout(frmHost)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcdNumber = QtGui.QLCDNumber(frmHost)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 0))
        self.lcdNumber.setBaseSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setLineWidth(10)
        self.lcdNumber.setMidLineWidth(-1)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout.addWidget(self.lcdNumber)
        self.line = QtGui.QFrame(frmHost)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.pushButton = QtGui.QPushButton(frmHost)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(frmHost)
        QtCore.QMetaObject.connectSlotsByName(frmHost)

    def retranslateUi(self, frmHost):
        frmHost.setWindowTitle(_translate("frmHost", "Form", None))
        self.pushButton.setText(_translate("frmHost", "PushButton", None))


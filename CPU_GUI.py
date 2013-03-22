# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPU_GUI.ui'
#
# Created: Fri Mar 22 17:19:53 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import psutil

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
        #-----------------
        self.ncore=0
        #self.lcd_name="lcd{}".format(self.ncore)
        #self.button_name="cmd{}".format(self.ncore)
        self.lcd =[]
        self.cmd=[]
        #-----------------
        
        self.verticalLayout = QtGui.QVBoxLayout(frmHost)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        for self.core in range (psutil.NUM_CPUS):
        
            lcdNumber = QtGui.QLCDNumber(frmHost)
            lcdNumber.setObjectName(_fromUtf8("lcd{}".format(self.core))) 
            self.lcd.append(lcdNumber)
            self.verticalLayout.addWidget(lcdNumber)
        
            pushButton = QtGui.QPushButton(frmHost)
            pushButton.setObjectName(_fromUtf8("cmd{}".format(self.core)))
            self.cmd.append(pushButton)
            self.verticalLayout.addWidget(pushButton)

        self.retranslateUi(frmHost)
        QtCore.QMetaObject.connectSlotsByName(frmHost)

    def retranslateUi(self, frmHost):
        frmHost.setWindowTitle(_translate("frmHost", "Form", None))
        for but in self.cmd:
            but.setText(_translate("frmHost", but.objectName(), None))


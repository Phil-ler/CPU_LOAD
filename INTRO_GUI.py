# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTRO_GUI.ui'
#
# Created: Wed Apr 10 10:45:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qt
import main
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

class Ui_MainWindow(object):
    def setupUi_2 (self,MainWindow):
        self.gridLayout = 0
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        for i in range (len(self.host_w)):
            host = main.Host_Widget(self.host_w[i].IP)
            self.gridLayout.addWidget(host)
    def setupUi(self, MainWindow):
        
        self.host_w = []
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        #TExt
       
        host = main.Host_Widget("LOCAL")
        self.host_w.append(host)
        self.gridLayout.addWidget(host)
        
        #self.lcd.append(lcdNumber)
        # self.verticalLayout.addWidget(lcdNumber)n
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Host = QtGui.QAction(MainWindow)
        self.actionAdd_Host.setObjectName(_fromUtf8("actionAdd_Host"))
        self.actionRemove_Host = QtGui.QAction(MainWindow)
        self.actionRemove_Host.setObjectName(_fromUtf8("actionRemove_Host"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionGeneral_Options = QtGui.QAction(MainWindow)
        self.actionGeneral_Options.setObjectName(_fromUtf8("actionGeneral_Options"))
        self.actionSave_Configuration = QtGui.QAction(MainWindow)
        self.actionSave_Configuration.setObjectName(_fromUtf8("actionSave_Configuration"))
        self.actionLoad_Configuration = QtGui.QAction(MainWindow)
        self.actionLoad_Configuration.setObjectName(_fromUtf8("actionLoad_Configuration"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionAdd_Host)
        self.menuFile.addAction(self.actionRemove_Host)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionGeneral_Options)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionSave_Configuration)
        self.menuSettings.addAction(self.actionLoad_Configuration)
        self.menu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "Host", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menu.setTitle(_translate("MainWindow", "?", None))
        self.actionAdd_Host.setText(_translate("MainWindow", "Add Host", None))
        self.actionRemove_Host.setText(_translate("MainWindow", "Remove Host", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionGeneral_Options.setText(_translate("MainWindow", "General Options", None))
        self.actionSave_Configuration.setText(_translate("MainWindow", "Save Configuration", None))
        self.actionLoad_Configuration.setText(_translate("MainWindow", "Load Configuration", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


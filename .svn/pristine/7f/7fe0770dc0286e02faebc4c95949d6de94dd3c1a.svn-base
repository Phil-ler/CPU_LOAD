# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CORE_GUI.ui'
#
# Created: Fri Apr  5 16:58:16 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Grafico
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

class Ui_frm_core(object):
    def setupUi(self, frm_core):
        frm_core.setObjectName(_fromUtf8("frm_core"))
        frm_core.setMinimumSize(800,400)
        self.verticalLayout = QtGui.QVBoxLayout(frm_core)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_core = QtGui.QLabel(frm_core)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_core.sizePolicy().hasHeightForWidth())
        self.lbl_core.setSizePolicy(sizePolicy)
        self.lbl_core.setObjectName(_fromUtf8("lbl_core"))
        self.verticalLayout.addWidget(self.lbl_core)
        #-----------------------------------------------------
        self.grafico = Grafico.Grafico()
        self.verticalLayout.addWidget(self.grafico)
        #-----------------------------------------------------
        
        self.lbl_carico = QtGui.QLabel(frm_core)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_carico.sizePolicy().hasHeightForWidth())
        self.lbl_carico.setSizePolicy(sizePolicy)
        self.lbl_carico.setObjectName(_fromUtf8("lbl_carico"))
        self.verticalLayout.addWidget(self.lbl_carico)

        self.retranslateUi(frm_core)
        QtCore.QMetaObject.connectSlotsByName(frm_core)

    def retranslateUi(self, frm_core):
        frm_core.setWindowTitle(_translate("frm_core", "Form", None))
        self.lbl_core.setText(_translate("frm_core", "TextLabel", None))
        self.lbl_carico.setText(_translate("frm_core", "<html><head/><body><p>Carico</p></body></html>", None))


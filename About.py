'''
Created on 27/giu/2013

@author: phil
'''
from PyQt4 import QtGui
import ABOUT_GUI
class About(QtGui.QDialog):
    '''
    QDialog About
    '''
    def __init__(self):
        super(About, self).__init__()
        self.ui = ABOUT_GUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setWindowTitle("About")
        self.ui.pushButton.clicked.connect(self.hide)
        
        
    def mostra (self):
        '''
        Mostra la Dialog "About"
        '''
        self.show();
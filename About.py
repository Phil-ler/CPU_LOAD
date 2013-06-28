'''
Created on 27/giu/2013

@author: phil
'''
from PyQt4 import QtGui
import ABOUT_GUI
class About(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(About, self).__init__()
        self.ui = ABOUT_GUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setWindowTitle("About")
        self.ui.pushButton.clicked.connect(self.hide)
        
        '''
        Mostra la Dialog "About"
        '''
        
    def mostra (self):
        self.show();
'''

'''
from PyQt4 import QtGui
import progress_GUI
class ProgressGui(QtGui.QMainWindow):
    '''
    QDialog About
    
    '''
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = progress_GUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setWindowTitle("Progress")
    
    def set_values (self,text,value):
        self.ui.lbl_progress.setText(text)
        self.ui.progressBar.setValue(value)
    
    def mostra (self):
        '''
        Mostra la Dialog "About"
        '''
        self.show();
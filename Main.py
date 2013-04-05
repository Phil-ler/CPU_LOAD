'''

Created on 20/mar/2013

@author: phil
'''
import psutil
from Host import Host
from PyQt4 import QtCore,QtGui
import CPU_GUI
import sys


class MainWindow(QtGui.QMainWindow):
    """
    Classe della finestra principale
    
    """
    chiusura =QtCore.pyqtSignal()
    def __init__(self):
        """
        Costruttore della classe MainWindow.
        
        """
        super(MainWindow, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CPU_GUI.Ui_frmHost()
        self.ui.setupUi(self.centralWidget())
        self.num_Host = psutil.NUM_CPUS
        self.My_Host = Host(self.num_Host,0.5)
        
        '''
        connettore pulsanti
        mostreranno le finestre dedicate a ogni singolo Core
        '''
        
        for i in range (self.num_Host):   
            self.ui.cmd[i].clicked.connect(self.My_Host.core[i].show)
            
        '''\
        crezione thread
        '''
        self._thread=QtCore.QThread(self)
        self.My_Host.moveToThread(self._thread) #muovo la classe Host dentro al thread
        self._thread.started.connect(self.My_Host.Run,2) #funzione che parte nel thread
        self.My_Host.ritorno_dati.connect(self.riempi) #quando dentro Host viene lanciato il segnale che son pronti i dati mostra dentro i LED
        self._thread.start()      
    
    def closeEvent(self,event):
        for i in range (self.num_Host):
            self.My_Host.core[i].hide()
        print("Finestre secondarie Chiuse")
        QtGui.QMainWindow.closeEvent(self,event)
        #ritorno_dati = PyQt4.QtCore.pyqtSignal(list)
        
        self.chiusura.emit()
        
        
    def riempi(self,carico):    
            
        for i in range(self.num_Host):
            self.ui.lcd[i].display(carico[i])
            self.My_Host.core[i].traccia()
    
    def prova(self):
    
        print("Sono qui")    


def main():
    print("CIAO")
    
    app = QtGui.QApplication(sys.argv)
    
    my_mainWindow = MainWindow()
    my_mainWindow.show()    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
'''

Created on 20/mar/2013

In questo modulo è presente

@author: phil
'''

from Core_Wallet import Core_Wallet
from PyQt4 import QtCore,QtGui
import CPU_GUI


class LocalHost(QtGui.QMainWindow):
    """
    Classe della finestra principale dell'host in questione
    
    """
    chiusura =QtCore.pyqtSignal()
    def __init__(self,IP,timer):
        """
        Costruttore della classe 
        
        """
        
        super(LocalHost, self).__init__()
        
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CPU_GUI.Ui_frmHost()
        self.ui.setupUi(self.centralWidget())
        self.timer=timer # selec
        self.My_Host = Core_Wallet(self.timer,IP)
        self.carico_generico = []
        
        self.num_Host = self.My_Host.get_N_cores()
        '''
        connettore pulsanti
        mostreranno le finestre dedicate a ogni singolo Core
        '''
        #print( self.num_Host)
        for i in range (self.num_Host):   
            self.ui.cmd[i].clicked.connect(self.My_Host.core[i].show)
            
        '''\
        crezione thread
        '''
        self._thread=QtCore.QThread(self)
        self._thread.setTerminationEnabled(True)
        self.My_Host.moveToThread(self._thread) #muovo la classe Core_Wallet dentro al thread
        self._thread.started.connect(self.My_Host.Run,2) #funzione che parte nel thread
        self.My_Host.ritorno_dati.connect(self.riempi) #quando dentro Core_Wallet viene lanciato il segnale che son pronti i dati mostra dentro i LED    
    
    def set_timer (self,timer):
        self.timer = timer
        
        self.My_Host.set_timer(self.timer)
            
        
    def start_thread (self):
        self._thread.start()
    
    def stop_thread (self):
        self._thread.stop()
    
    def closeEvent(self,event):
        for i in range (self.num_Host):
            self.My_Host.core[i].hide()
        print("Finestre secondarie Chiuse")
        QtGui.QMainWindow.closeEvent(self,event)
        self.chiusura.emit()
        
        
    def riempi(self,carico):    
        
       
        for i in range(self.num_Host):
            
            self.ui.lcd[i].display(carico[i])
            self.My_Host.core[i].traccia()
    
    def prova(self,dove):
    
        print("Sono qui ->"+dove)    

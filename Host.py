# -*- coding: iso-8859-15 -*-
'''
Created on 20/mar/2013

In questo modulo è presente

@author: phil
'''

from Core_Wallet import Core_Wallet
from PyQt4 import QtCore,QtGui
import CPU_GUI


class Host(QtGui.QMainWindow):
    """
    Classe della finestra principale dell'host in questione
    """
    chiusura =QtCore.pyqtSignal()
    def __init__(self,IP,timer):
        
        super(Host, self).__init__()
        
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CPU_GUI.Ui_frmHost()
        self.ui.setupUi(self.centralWidget())
        self.timer=timer # selec
        self.Host_Cores = Core_Wallet(self.timer,IP)
        self.carico_generico = []
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.num_Host = self.Host_Cores.get_N_cores()
        self.setWindowTitle("Core Pool")
        
        #connettore pulsanti
        #mostreranno le finestre dedicate a ogni singolo Core
        
        #print( self.num_Host)
        for i in range (self.num_Host):   
            self.ui.cmd[i].clicked.connect(self.Host_Cores.core[i].show)
            
        
        #crezione thread
        
        self._thread=QtCore.QThread(self)
        self._thread.setTerminationEnabled(True)
        self.Host_Cores.moveToThread(self._thread) #muovo la classe Core_Wallet dentro al thread
        self._thread.started.connect(self.Host_Cores.Run,2) #funzione che parte nel thread
        self.Host_Cores.ritorno_dati.connect(self.riempi) #quando dentro Core_Wallet viene lanciato il segnale che son pronti i dati mostra dentro i LED    
    
   
    
    def set_timer (self,timer):
        '''
    Setta il timer di aggiornamento a tutte le istanze Core presenti nel programma
    @param timer: Float che indica la frequenza
    '''
        self.timer = timer
        
        self.Host_Cores.set_timer(self.timer)
            
        
    def start_thread (self):
        '''
    Fa partire il thread di monitoraggio
    '''
        self._thread.start()

    def stop_thread (self):
        '''
    Ferma il thread
    '''
        self._thread.stop()
    
    def __closeEvent(self,event):
        for i in range (self.num_Host):
            self.Host_Cores.core[i].hide()
        print("Finestre secondarie Chiuse")
        QtGui.QMainWindow.closeEvent(self,event)
        self.chiusura.emit()
        
       
    def riempi(self,carico):    
        '''
    Funzione che riceve i dati letti del processore
    @param carico: Lista di valori contenenti i valori letti dalla CPU
    ''' 
       
        for i in range(self.num_Host):
            
            self.ui.lcd[i].display(carico[i])
            self.Host_Cores.core[i].traccia()
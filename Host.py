# -*- coding: iso-8859-15 -*-
'''
Created on 20/mar/2013

In questo modulo é presente
'''

from Core_Wallet import Core_Wallet
from PyQt4 import QtCore,QtGui
import CPU_GUI
#import monitoraggio


class Host(QtGui.QMainWindow):
    '''
    Classe della finestra principale dell'host in questione
    @author Filippo Verucchi
    '''
    chiusura =QtCore.pyqtSignal()
    def __init__(self,IP,timer,ID,passwd = None):
        
        super(Host, self).__init__()
        
        self.setCentralWidget(QtGui.QWidget(self))
        self.timer=timer # selec
        self.ID = ID
        self.Host_Cores = Core_Wallet(self.timer,IP,ID,passwd)
        self.carico_generico = []
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.num_Cores = self.Host_Cores.get_N_cores()
        self.ui = CPU_GUI.Ui_frmHost()
        self.ui.setupUi(self.centralWidget(),self.num_Cores)
        #self.monitor = monitoraggio.Monitoraggio(IP,self.num_Cores)
        self.setWindowTitle("Core Pool {}".format(IP))
        '''
        self.ui.cmdMonitor.clicked.connect(self.monitor.show)
        '''
        #connettore pulsanti
        #mostreranno le finestre dedicate a ogni singolo Core
        
        #print( self.num_Cores)
        for i in range (self.num_Cores):   
            self.ui.cmd[i].clicked.connect(self.Host_Cores.core[i].show)
        
        #crezione thread
        self._thread=QtCore.QThread(self)
        self._thread.setTerminationEnabled(True)
        self.Host_Cores.moveToThread(self._thread) #muovo la classe Core_Wallet dentro al thread
        self._thread.started.connect(self.Host_Cores.Run,2) #funzione che parte nel thread
        
        self.Host_Cores.ritorno_dati.connect(self.riempi) #quando dentro Core_Wallet viene lanciato il segnale che son pronti i dati mostra dentro i LED    
        
        #dati da monitorare
        #self.monitor_data = []
        #print("FINE HOST")
        
    #def clear_monitor (self):
    #    self.monitor_data = []
    
    def set_timer (self,timer):
        '''
        Setta il timer di aggiornamento a tutte le istanze Core presenti nel programma
        @param timer: Float che indica la frequenza
        '''
        self.timer = timer
        
        self.Host_Cores.set_timer(self.timer)
            
    def start_thread (self):
        '''
        Starta il tread di lettura
        
        '''
        self._thread.start()

    def stop_thread (self):
        '''
        Ferma il tread di lettura
        
        '''
        self._thread.stop()
    
    def closeEvent(self,event):
        '''
        Override di closeEvent, chiude tutte le finestre attive e termina le comunicazioni
        '''
        for i in range (self.num_Cores):
            self.Host_Cores.core[i].hide()
        #self.monitor.hide()
        print("Finestre secondarie Chiuse")
        QtGui.QMainWindow.closeEvent(self,event)
        self.chiusura.emit()
        
       
    def riempi(self,carico):    
        '''
        Funzione che riceve i dati letti del processore
        @param carico: Lista di valori contenenti i valori letti dalla CPU
        ''' 
        
        for i in range(self.num_Cores):
            
            self.ui.lcd[i].display(carico[i])
            self.Host_Cores.core[i].traccia()
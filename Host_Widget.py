# -*- coding: iso-8859-15 -*-
import Host
from PyQt4 import QtCore, QtGui, Qt

'''
Created on 26/apr/2013
Classe Host_Widget, estende un Button in quanto facendosi click sopra, si apre la finestra dedicata all'host in questione

@author: Filippo Verucchi
'''
class Host_Widget (QtGui.QPushButton):
    
    def __init__(self,IP,Main):
        super(Host_Widget, self).__init__()
        self.Main = Main
        self.IP=IP
        self.timer = self.Main.freq
        self.ping_True = False
        self.local = Host.Host(self.IP,self.timer)
        
       
        self.clicked.connect(self.show_window)
        self.local.Host_Cores.valore_generico.connect(self.show_generic_load)
        self.carico = 0
        
        self.local.Host_Cores.connection_lost.connect(self.Main.elimina_host)
        self.local.Host_Cores.connection_ok.connect(self.Ping_ON)
    
    
    def set_freq (self,freq):
        '''
        Gli viene passata la frequenza di aggiornamento timer dalle impostazioni setta il timer sull'host
        @param freq: Timer di aggiornamento
        '''
        self.timer = freq
        self.local.set_timer(self.timer)
    
    def Ping_ON (self):
        '''
        Se la connessione è attiva fa partire il thread
        '''
        
        self.ping_True= True

    def Ping_Off (self):
        '''
        Se la connessione cade blocca il thread di aggiornamento
        '''
        self.ping_True = False
    

        
    def paintEvent(self, event):
        '''
        Paint-Event di Host_Widget
        '''
       
        qp = QtGui.QPainter()
        qp.begin(self)
        #qp.setRenderHint(QtGui.QPainter.Antialiasing)
        #qp.setPen(QtCore.Qt.green)
        #qp.drawText(50,50,"{}".format(percent))
       
        if (self.ping_True==False and self.IP != "LOCAL"):
            qp.setBrush(Qt.QBrush(QtCore.Qt.gray))
        elif self.carico < 40:
            qp.setBrush(Qt.QBrush(QtCore.Qt.green))
        elif self.carico <80:
            qp.setBrush(Qt.QBrush(QtCore.Qt.yellow))
        else:
            qp.setBrush(Qt.QBrush(QtCore.Qt.red))
  
        qp.drawRect(0,0,self.width(),self.height())
        qp.setPen(QtCore.Qt.black)
        qp.drawText(20,20, "{} - {}".format(self.IP,self.carico))
    
       
    def show_window(self):
        '''
        Mostra la finestra con le informazioni dell'host
        ''' 
        self.local.start_thread()
        self.local.Host_Cores.set_Start()
        self.local.show()
   
    def show_generic_load (self,carico):
        '''
        Dato il carico generico dell'host, lo mostra a video
        '''
        self.carico= carico
        self.repaint()
        #print(("Carico {}".format(carico)))
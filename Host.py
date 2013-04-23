'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
import psutil
from Analizzatore import Analizzatore
from Pyro4 import *


from PyQt4 import QtCore, QtGui
import Pyro4
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Host(QtCore.QObject):
 
       
    #Questo è il segnale
    ritorno_dati = QtCore.pyqtSignal(list)
    valore_generico = QtCore.pyqtSignal(float)
    connection_lost = QtCore.pyqtSignal()
    connection_ok =QtCore.pyqtSignal()
    def __init__(self,timer,IP):
        '''
        Constructor
        '''
        
        QtCore.QObject.__init__(self)
        
        self.core = []
        self.win_core = []
        self.timer = timer
        self.start_T=True
        print("Prima del naming")
        self.IP = IP
        Pyro4.COMMTIMEOUT = 3
        if (IP == "LOCAL"):
            self.analizzatore = Analizzatore()
        else:
            try:
                Pyro4.config.COMMTIMEOUT = 1.5  
                #host =str(IP)
                ns = naming.locateNS(str(IP))
                #ns._pyroTimeout = 4
                #localizza il DNS nell'IP che gli passo, ovvero sulla macchina server
                print("cercato il nameserver")
                uri=ns.lookup("CPU_LOAD")
                print("URI PRESO {}".format(uri))
                (preuri,posturi) = uri.asString().split(sep="@")
                (address, port ) = posturi.split(sep=":")
                uri =(preuri +"@"+ str(IP) +":" + port)
               
                self.analizzatore = Proxy(uri)
                #print ("Numero CORE ",thing.get_n_core())
            except errors.NamingError:
                print("NameServer non trovato")
                return
           
        self.Num_Cores= self.analizzatore.get_n_core()
        for i in range(self.Num_Cores):
            self.core.append(Core(i))
            print("Core creato n°",i)
    
    
    def fill (self,percent):
        for i in range(self.Num_Cores):
            #print ("Carico del processore ",percent[c])
            self.core[i].load(percent[i])
    
    def get_N_cores (self):
        return self.Num_Cores
    
    def set_Stop(self):
        self.start_T=False            
    def set_Start (self):
        self.start_T= True
               
    def Run(self):
        while(self.start_T):
            try:
                percent = self.analizzatore.get_cores_values()
            
                media =self.analizzatore.get_generic()
                print(percent)
                #riempi ogni singolo Core
                self.fill(percent) 
            
                #emette il segnale, ritornando percent
                self.ritorno_dati.emit(percent)
                self.valore_generico.emit(media)
                self.connection_ok.emit()
                
                #return percent
            except Pyro4.errors.ConnectionClosedError:
                self.set_Stop()
                self.connection_lost.emit()
                #self.ERRORE("Persa la connessione col server")
                
                return


        '''
    ESEMPIO DI CLIENT!!!
import Pyro4
Host = "192.168.3.180"
ns = Pyro4.naming.locateNS(host = Host)
uri=ns.lookup("CPU_LOAD")
(preuri,posturi) = uri.asString().split(sep="@")
(address, port ) = posturi.split(sep=":")
uri = preuri +"@"+ Host +":" + port
thing = Pyro4.Proxy(uri)
print ("Numero CORE ",thing.get_n_core())


'''
                
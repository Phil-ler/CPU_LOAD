'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
import psutil
from Analizzatore import Analizzatore
import Pyro4

from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Host(QtCore.QObject):
 
       
    #Questo è il segnale
    ritorno_dati = QtCore.pyqtSignal(list)
    valore_generico = QtCore.pyqtSignal(float)
    
    def __init__(self,timer,IP):
        '''
        Constructor
        '''
        
        QtCore.QObject.__init__(self)
        
        self.core = []
        self.win_core = []
        self.timer = timer
        self.start_T=True
        
        if (IP == "LOCAL"):
            self.analizzatore = Analizzatore()
        else:
            
            
            ns = Pyro4.naming.locateNS(host =str(IP))
            uri=ns.lookup("CPU_LOAD")
            print("URI PRESO {}".format(uri))
            (preuri,posturi) = uri.asString().split(sep="@")
            (address, port ) = posturi.split(sep=":")
            uri =(preuri +"@"+ str(IP) +":" + port)
            self.analizzatore = Pyro4.Proxy(uri)
            #print ("Numero CORE ",thing.get_n_core())

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
         
    def Run(self):
        while(True):
            
            percent = self.analizzatore.get_cores_values()
            
            media =self.analizzatore.get_generic()
            print(percent)
            #riempi ogni singolo Core
            self.fill(percent) 
            
            #emette il segnale, ritornando percent
            self.ritorno_dati.emit(percent)
            self.valore_generico.emit(media)
            #return percent



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
                
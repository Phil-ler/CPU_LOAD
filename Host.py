'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
import psutil

from PyQt4 import QtCore
import PyQt4
class Host(QtCore.QObject):
 
       
    #Questo è il segnale
    ritorno_dati = PyQt4.QtCore.pyqtSignal(list)
    valore_generico = PyQt4.QtCore.pyqtSignal(float)
    
    def __init__(self,Num_Cores,timer):
        '''
        Constructor
        '''
        
        QtCore.QObject.__init__(self)
        self.Num_Cores=Num_Cores
        self.core = []
        self.win_core = []
        self.timer = timer
        self.stop=True
        for i in range(self.Num_Cores):
            self.core.append(Core(i))
            print("Core creato n°",i)
            
    def fill (self,percent):
        for i in range(self.Num_Cores):
            #print ("Carico del processore ",percent[c])
            self.core[i].load(percent[i])
    
    def set_Stop(self):
        self.stop=False                   
         
    def Run(self):
        while(self.stop):
            
            percent=psutil.cpu_percent(interval=self.timer, percpu=True)
            media =psutil.cpu_percent()
            print(percent)
            #riempi ogni singolo Core
            self.fill(percent) 
            
            #emette il segnale, ritornando percent
            self.ritorno_dati.emit(percent)
            self.valore_generico.emit(media)
            #return percent
        
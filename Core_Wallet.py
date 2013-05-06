'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
from Analizzatore import Analizzatore
import time
from PyQt4 import QtCore, QtGui
import Pyro4
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

'''
Classe che raccoglie i dati da tutti i core presenti nell'Host e li cede alla classe Host per essere visualizzati e alla classe Grafico per essere disegnati
Inoltre crea la connessione con il server designato se il nome dell'Host è diverso da LOCAL, altrimenti esegue solo una scansione locale senza l'utilizzo del server
'''
class Core_Wallet(QtCore.QObject):
 
       
    #Raccolta segnali
    ritorno_dati = QtCore.pyqtSignal(list)
    valore_generico = QtCore.pyqtSignal(float)
    connection_lost = QtCore.pyqtSignal(str,str)
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
        #print("Prima del naming")
        self.IP = IP
        Pyro4.COMMTIMEOUT = 3
        if (IP == "LOCAL"):
            self.analizzatore = Analizzatore()
        else:
            try:
                Pyro4.config.COMMTIMEOUT = 1.5  
                #host =str(IP)
                ns = Pyro4.naming.locateNS(str(IP))
                #ns._pyroTimeout = 4
                #localizza il DNS nell'IP che gli passo, ovvero sulla macchina server
                print("cercato il nameserver")
                uri=ns.lookup("CPU_LOAD")
                print("URI PRESO {}".format(uri))
                (preuri,posturi) = uri.asString().split(sep="@")
                (address, port ) = posturi.split(sep=":")
                uri =(preuri +"@"+ str(IP) +":" + port)
               
                self.analizzatore = Pyro4.Proxy(uri)
                #print ("Numero CORE ",thing.get_n_core())
            except Error.NamingError:
                print("NameServer non trovato")
                return
           
        self.__Num_Cores= self.analizzatore.get_n_core()
        for i in range(self.__Num_Cores):
            self.core.append(Core(i))
            print("Core creato n°",i)
    
    '''
    Quando i valori dei core sono stati letti, questa funzione viene chiamata per riempire i vari campi di lettura
    '''    

    def fill (self,percent):
        for i in range(self.__Num_Cores):
            #print ("Carico del processore ",percent[c])
            self.core[i].load(percent[i])
    '''
    Ritorna il numero di core presenti nell'Host
    '''
    
    def get_N_cores (self):
        return self.__Num_Cores
    '''
    Ferma il ciclo di lettura
    '''
    def set_Stop(self):
        self.start_T=False   
    '''
    Starta il ciclo di letture
    '''         
    def set_Start (self):
        self.start_T= True
    '''
    Setta il timer di frequenza di lettura
    '''
    def set_timer(self,timer):
        self.timer = timer
    
    '''
    Funzione legge dalla classe Analizzatore i carichi delle CPU secondo il timer dato e riempe i campi di lettura con la funzione "fill"
    '''
     
    def Run(self):
        while(self.start_T):
            try:
                
                time.sleep(self.timer)
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
                self.connection_lost.emit(self.IP,"Persa la connessione col server - Il collegamento verrà rimosso")
                #self.ERRORE("Persa la connessione col server")
                
                return

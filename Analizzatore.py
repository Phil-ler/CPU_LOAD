# -*- coding: iso-8859-15 -*-
'''
Created on 15/apr/2013

@author: phil
'''

import Pyro4
import threading
import time
import signal
import sys
import psutil


class Analizzatore():
    '''
    Classe che legge, tramite la libreria psutil, i valori di carico della CPU
    '''
    
    def __init__(self):
       
        self.carico_core = []
        
        self.generic = []        
        self.N_CORES=psutil.NUM_CPUS
        
    def get_n_core (self):
        '''
        Ritorna il numero di Core di cui é composta la CPU
        '''
    
        return self.N_CORES
    
    def get_cores_values (self):
        '''
        Ritorna la lista contenente i valori attuali di tutti i core
        '''
        self.carico_core = psutil.cpu_percent(percpu=True)
    
        return self.carico_core
    
    def get_generic (self,timer):
        '''
        Ritorna la lista contenente la media dei valori di tutti i core dell'HOST
        @return: Carico generico
        '''
    
        self.generic = psutil.cpu_percent(interval=timer, percpu=False)
        return self.generic
   
        
   
class _Dati_Server ():
   
    '''
    Classe che raccoglie i dati del server per la connessione
    ''' 
    def __init__(self,Daemon,Thread,NS):
    
        self.Daemon= Daemon
        self.Thread = Thread
        self.NS = NS
    
    def signal_handler(self,signal, frame):
        '''
        Chiude il server quando viene mandato il segnale di CTRL-C
        '''
    
        print ("Chiusura Server")
        #self.Thread.join(0.1)
        #print(self.NS.list())
        #self.Daemon.shutdown()
        self.Thread._stop()
        print("Server Chiuso!")
        
        sys.exit(0)

def startNSserverLoop():
    '''
    Starta il server
    '''
    NSThread = threading.Thread(target=Pyro4.naming.startNSloop,args=[])
    NSThread.start()
    return NSThread

def main():
    """
    Funzione principale per avviare il server.
    Fa partire un Name Server Pyro e ci registra sopra un oggetto ServerProcessor

    """ 
    
    
    IP = "0.0.0.0"
    
    print(" IP RANGE =,",IP)
    #analizer = Analizer.Analizer("")
    A=Analizzatore()
    
    
    Pyro4.config.HOST = IP
    try:
        nsThread=startNSserverLoop()
        time.sleep(1)
        ns=Pyro4.naming.locateNS("localhost")
    
        print(ns)
        ns.ping()
        print(ns)
    
        daemon=Pyro4.Daemon()
        uri=daemon.register(A)
    
        ns.register("CPU_LOAD",uri)
        D = _Dati_Server(daemon,nsThread,ns)
        signal.signal(signal.SIGINT, D.signal_handler)
    
        print ("Object uri = {0}".format(uri))
        print ("Ready")
    
        daemon.requestLoop()
    except Pyro4.errors.CommunicationError:
        print("Error! IP Range not correct, Server not started !!!")
    
if __name__ == "__main__":
    
    main()

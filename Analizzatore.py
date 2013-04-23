'''
Created on 15/apr/2013

@author: phil
'''
import psutil
import Pyro4
import threading
import time
import signal




class Analizzatore():
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.N_CORES =0
        self.carico_core = []
        self.timer = 0.1 # da mettere nel config
        self.generic = 0        
        self.N_CORES=psutil.NUM_CPUS
    def get_n_core (self):
        
        print("Analizzatore segna #core ->", self.N_CORES)
        return self.N_CORES
    
    def get_cores_values (self):
        
        self.carico_core = psutil.cpu_percent(percpu=True)
    
        return self.carico_core
    
    def get_generic (self):
        self.generic = psutil.cpu_percent(interval=self.timer, percpu=False)
        return self.generic
    
    def set_timer (self,timer):
        self.timer = timer
        
   
    
class Dati_Server ():
    
    def __init__(self,Daemon,Thread,NS):
        '''
        Constructor
        '''
        self.Daemon= Daemon
        self.Thread = Thread
        self.NS = NS
    
    
    def signal_handler(self,signal, frame):
        print ("Chiusura Server")
        #self.Thread.join(0.1)
        #print(self.NS.list())
        #self.Daemon.shutdown()
        self.Thread._stop()
        print("Server Chiuso!")
        
        sys.exit(0)
def startNSserverLoop():
        
    NSThread = threading.Thread(target=Pyro4.naming.startNSloop,args=[])
    NSThread.start()
    return NSThread

def main():
    """
    Funzione principale per avviare il server.
    Fa partire un Name Server Pyro e ci registra sopra un oggetto ServerProcessor

    """ 
    #analizer = Analizer.Analizer("")
    A=Analizzatore()
    
    
    Pyro4.config.HOST = "0.0.0.0"
    try:
        nsThread=startNSserverLoop()
        print("Thread creato, ora aspetto 5 secondi")
        time.sleep(0.5)
        ns=Pyro4.naming.locateNS("localhost")
    
        print(ns)
        ns.ping()
        print(ns)
    
        daemon=Pyro4.Daemon()
        uri=daemon.register(A)
    
        ns.register("CPU_LOAD",uri)
        D = Dati_Server(daemon,nsThread,ns)
        signal.signal(signal.SIGINT, D.signal_handler)
    
        print ("Object uri = {0}".format(uri))
        print ("Ready")
    
        daemon.requestLoop()
    except Pyro4.errors.CommunicationError:
        print("ASD!!!")
    
if __name__ == "__main__":
    
    main()
'''
Created on 15/apr/2013

@author: phil
'''
import psutil
import Pyro4
import sys
import threading
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
        self.timer = 0.1
        self.generic = 0        
    
    def get_n_core (self):
        self.N_CORES=psutil.NUM_CPUS
        return self.N_CORES
    
    def get_cores_values (self):
        
        self.carico_core = psutil.cpu_percent(percpu=True)
    
        return self.carico_core
    
    def get_generic (self):
        self.generic = psutil.cpu_percent(interval=self.timer, percpu=False)
        return self.generic
    
    def set_timer (self,timer):
        self.timer = timer
        
def startNSserverLoop():
        
    NSThread = threading.Thread(target=Pyro4.naming.main,args=[[]])
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
    nsThread=startNSserverLoop()
    ns=Pyro4.naming.locateNS("localhost")
    
    print(ns)
    ns.ping()
    print(ns)
    
    daemon=Pyro4.Daemon()
    uri=daemon.register(A)
    
    ns.register("CPU_LOAD",uri)
    
    print ("Object uri = {0}".format(uri))
    print ("Ready")
    
    daemon.requestLoop()
    
    
if __name__ == "__main__":
    main()
    
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
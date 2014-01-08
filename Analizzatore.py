# -*- coding: iso-8859-15 -*-
'''
Created on 15/apr/2013

@author: phil
'''

import Pyro4
import argparse
import signal
import sys
import psutil
import socket
'''
Questo e' il file server necessario alla comunicazione remota, eseguendolo viene registrato sulla macchina remota
un pyro object rappresentante l'oggetto addetto alla lettura dei carichi il quale viene poi registrato in rete
sul nameserver per renderlo reperibile dal programma principale con funzione di client.
'''

class Analizzatore():
    
    '''
    Classe che legge, tramite la libreria psutil, i valori di carico della CPU
    @author Filippo Verucchi
    '''
    def __init__(self):
       
        self.carico_core = []
        
        self.generic = []        
        self.N_CORES=psutil.NUM_CPUS
    
    
        
    def get_n_core (self):
        '''
        Ritorna il numero di Core di cui é composta la CPU
        @retval Numero dei CPU_Cores della macchina.
        '''
    
        return self.N_CORES
    
    def get_cores_values (self):
        '''
        Ritorna la lista contenente i valori attuali di tutti i core
        @retval lista valori letti
        '''
        self.carico_core = psutil.cpu_percent(percpu=True)
    
        return self.carico_core
    
    def get_generic (self,timer):
        '''
        Ritorna la lista contenente la media dei valori di tutti i core dell'HOST
        @param timer: Frequenza di lettura CPU
        @return Carico generico
        '''
    
        self.generic = psutil.cpu_percent(interval=timer, percpu=False)
        return self.generic
   
    def get_IP(self):
        '''
        Metodo che ritorna l'ip della macchina locale.
        @retval: IP della macchina connessa in rete
        '''
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        IP = str(s.getsockname()[0])
        s.close()
        print(IP)
        return IP
    
    
    def get_Hostname(self):
        '''
        Metodo che ritorna l'hostname della macchina locale.
        @retval: hostname locale
        '''
        return socket.gethostname()
   

def stopConnection_handler(signal, frame):
    '''
    Metodo utilizzato dal main per chiudere correttamente la comunicazione con il nameserver e la macchina locale
    @param signal: parametro utilizzato dal signal handler per identificare il segnale di macchina catturato
    @param frame: frame che contiene l'applicazione in esecuzione da terminare
    '''
    print("Closing connection")
    ns.remove(pyroObjName)
    sys.exit(0)


def main():
   
    '''
    Metodo main del file server per la connessione remota.
    '''
    global ns
    global pyroObjName
    
    
    parser= argparse.ArgumentParser(description="Startup value settings")
    parser.add_argument("-i","--id", help="Set id for pyro object registration ")
    parser.add_argument("-n","--ns", help="Set the nameserver address (IP)")
    args = parser.parse_args()

    if args.id != None:
        ID= str(args.id)
    else:
        ID= ""
    
    if args.ns != None:
        NS_ID = str(args.ns)
    else:
        NS_ID = ""
        
    print("Lettura ID"+str(ID))
    
    analizzatore =Analizzatore()
    try:
        #Pyro4.config.HOST= "0.0.0.0"
        if NS_ID != "":
            print("Numero id definito "+NS_ID)
            ns= Pyro4.naming.locateNS(NS_ID)
        else:
            ns= Pyro4.naming.locateNS()
        
        print("NS ->{}".format(ns))
        pyroObjName= "CPU_LOAD"+str(ID)

        #daemon= Pyro4.Daemon()
        daemon= Pyro4.Daemon(analizzatore.get_IP())
        try:
            Analizzatore_uri=ns.lookup(pyroObjName)
            ns.remove(pyroObjName)
        except:
            pass

        Analizzatore_uri= daemon.register(analizzatore)
        
        ns.register(pyroObjName, Analizzatore_uri)

        print ("CPU_LOAD uri = {0}".format(Analizzatore_uri))
        print ("Ready")

        signal.signal(signal.SIGINT, stopConnection_handler )
        signal.signal(signal.SIGTERM, stopConnection_handler)

        daemon.requestLoop()

    except Pyro4.naming.NamingError as e:
        print (e)


if __name__ == "__main__":
    __doc__='''
    Questo e' il file server necessario alla comunicazione remota, eseguendolo viene registrato sulla macchina remota
    un pyro object rappresentante l'oggetto addetto alla lettura dei carichi il quale viene poi registrato in rete
    sul nameserver per renderlo reperibile dal programma principale con funzione di client.
@author: Filippo Verucchi
    '''
    main() 
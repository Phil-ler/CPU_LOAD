# -*- coding: iso-8859-15 -*-
'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
from Analizzatore import Analizzatore
import time
from PyQt4 import QtCore, QtGui
import monitoraggio
import Pyro4
import paramiko
import socket

 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Core_Wallet(QtCore.QObject):
 
    '''
    Classe che raccoglie i dati da tutti i core presenti nell'Host e li cede alla classe Host per essere visualizzati e alla classe Grafico per essere disegnati
    Inoltre crea la connessione con il server designato se il nome dell'Host è diverso da LOCAL, altrimenti esegue solo una scansione locale senza l'utilizzo del nameserver
    @author Filippo Verucchi
    ''' 
    #Raccolta segnali
    ritorno_dati = QtCore.pyqtSignal(list)
    valore_generico = QtCore.pyqtSignal(float)
    connection_lost = QtCore.pyqtSignal(int,str)
    connection_ok =QtCore.pyqtSignal()
    
    def __init__(self,timer,address,ID,passwd):
     
        QtCore.QObject.__init__(self)
        
        self.core = []
        self.win_core = []
        self.timer = timer
        #print("Prima del naming")
        self.address = address
        self.ID = ID
        self.passwd = passwd
        Pyro4.COMMTIMEOUT = 3
        self.getInfoHost() 
        
        time.sleep(2)
        self.__Num_Cores= self.analizzatore.get_n_core()
        self.core = []
        for i in range(self.__Num_Cores):
            self.core.append(Core(i))
            print("Core creato n°",i)
    
        #Creazione zona monitoraggio
        #self.Monitor = monitoraggio.Monitoraggio(self.__Num_Cores,address)
        
        #inizializzazione parametri utili per la lettura dei carichi di host
        self.authOk= False
        self.connection_Ok= False
        
    def get_IP(self):
        '''
        Metodo che ritorna l'ip della macchina locale.
        @return hostname locale
        '''
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        IP = str(s.getsockname()[0])
        s.close()
        print(IP)
        return IP
        

    
    def getInfoHost(self):
        '''
	Funzione che attiva il monitoraggio della macchina. 
	Se si esegue il monitoraggio Offline viene dichiarata un istanza Analizzatore,
	altrimenti ci si connette alla macchina remota
	'''
        if (self.address == "LOCAL"):
            self.analizzatore = Analizzatore()
            self.start_T=True
        else:
            print("NO LOCAL")
            self.ConnectHost()
            
    def OpenServerConnection(self):
        '''
        Si tenta di instaurare una connessione all'host remoto.
        Vengono passati alla macchina remota, tramite le paramiko, tutti i moduli necessari per la funzionalità del programma
        '''
        
        print("ID = "+str(self.ID))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if str(self.address).__contains__("@"):
                (username,hostname) = str(self.address).split("@")
                print("User = {}, host = {}".format(username,hostname))
                print("Tentativo connessione")
                
                ssh.connect(str(hostname),username=username, password= str(self.passwd),timeout = 5,allow_agent=False)
                addressToConnect = hostname
                
            else:
                ssh.connect(str(self.address), password = str(self.passwd),timeout=5,allow_agent=False)
                addressToConnect = self.address
            print("Connessione a "+str(hostname))
            self.authOk=True
            
            IP_NS = self.get_IP()
            sftp = ssh.open_sftp()
            print("Aperta connessione sftp")     
            print("Passo Analizzatore")
            sftp.put("Analizzatore.py","./Analizzatore.py")
            print("Passo Pyro4")
            sftp.put("Pyro4.tar.gz","./Pyro4.tar.gz") 
            print("Estraggo Pyro4")
            stdin, stdout, stderr= ssh.exec_command("tar -xzvf Pyro4.tar.gz")
            time.sleep(5)
            stdin, stdout, stderr= ssh.exec_command("echo $$; exec python3 Analizzatore.py --id {} --ns {}".format(self.ID,IP_NS))
            print("Esecuzione Analizzatore")
            self.remotePID= int(stdout.readline())
            print("PID Analizzatore {}".format(self.remotePID))
            time.sleep(1)
            #sftp.remove("Analizzatore.py")
            sftp.close()
            ssh.close()
           
            
            return addressToConnect
        
        except (paramiko.AuthenticationException, socket.error) as e:
            self.authOk= False
            ssh.close()
            print("connessione fallita:")
            print(e)
    
    def closeSSHConnection(self):
        '''
        Metodo che si occupa di chiudere la connessione in corso con l'host, stoppando ed eliminando il file in
        esecuzione che permette la registrazione dell'host stesso in rete allo scopo di ottenere le informazioni
        necessarie per visualizzare i carichi della CPU.
        Questa funzione viene chiamata anche in caso di errore di autenticazione (password errata, indirizzo errato o altro).
        '''
        ssh= paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if str(self.address).__contains__("@"):
                (username,hostname)= str(self.address).split("@")
                ssh.connect(str(hostname),username= username, password= str(self.passwd), timeout= 5,allow_agent=False)
            else:
                ssh.connect(str(self.address), password= str(self.passwd), timeout= 5,allow_agent=False)
            
            self.host = hostname
            print("Pid da cancellare"+str(self.remotePID))
            ssh.exec_command ("kill -s 15 {}".format(self.remotePID))
            
            ssh.exec_command("rm -r Pyro4*")
            ssh.exec_command("rm -r Analizzatore.py")
            
            time.sleep(1)
            
            ssh.close()

        except (paramiko.AuthenticationException, socket.error) as e:
            ssh.close()
            print("connessione fallita: autenticazione non riuscita") + "\n" + str(e)

     
    def ConnectHost(self):
        '''
        Reperisce il pyroObject remoto registrato sul NameServer per ottenere le info sull'Host
        '''        
        pyroObject = str(self.OpenServerConnection())
        
        if (self.authOk == True):
            try:
                ns = Pyro4.naming.locateNS()
                print("authOk")
                AnalizzatoreUri = ns.lookup("CPU_LOAD"+str(self.ID))
                print("CPUAnalyzer URI found at {}".format(AnalizzatoreUri))
                '''
                (uri,hostname) = AnalizzatoreUri.asString().split("@")
                (address,port) = hostname.split(":")
                AnalizzatoreUri = (uri+"@"+pyroObject+":"+port)
                '''
                print(AnalizzatoreUri)
                self.analizzatore = Pyro4.Proxy(AnalizzatoreUri)
                self.connection_2_ok=True
                self.start_T=True
                
            except Pyro4.errors.NamingError as E:
                self.connection_2_ok=False
                self.start_T=False
                print(str(E))
                self.closeSSHConnection()
                return
    
    def fill (self,percent):
        '''
        Quando i valori dei core sono stati letti, questa funzione viene chiamata per riempire i vari campi di lettura
        '''    

        for i in range(self.__Num_Cores):
            #print ("Carico del processore ",percent[c])
            self.core[i].load(percent[i])
    
    def get_N_cores (self):
        '''
        Ritorna il numero di core presenti nell'Host
        @return Numero di Cores
        '''
        return self.__Num_Cores
    
    def set_Stop(self):
        '''
        Ferma il ciclo di lettura
        '''
        self.start_T=False   
            
    def set_Start (self):
        '''
        Starta il ciclo di letture
        ''' 
        self.start_T= True

    def set_timer(self,timer):
        '''
        Setta il timer di frequenza di lettura
        '''
        self.timer = timer
    
     
    def Run(self):
        '''
        Funzione legge dalla classe Analizzatore i carichi delle CPU secondo il timer dato e riempe i campi di lettura con la funzione "fill"
        '''
    
        while(self.start_T):
            try:
                
                time.sleep(self.timer)
                percent = self.analizzatore.get_cores_values()
            
                media =self.analizzatore.get_generic(self.timer)
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
                self.connection_lost.emit(self.ID,"Persa la connessione col server - Il collegamento verrà  rimosso")
                #self.ERRORE("Persa la connessione col server")
                
                return

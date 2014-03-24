# -*- coding: iso-8859-15 -*-
'''
Created on 09/apr/2013

Modulo Principale che contiene il main() del programma

@author: phil

'''
import Option
from PyQt4 import QtGui, Qt
import INTRO_GUI
import sys
import About
import Pyro4
import time
import threading
import socket
import webbrowser
from Host_Widget import Host_Widget
import argparse 
   
   
def startNameServer():
    '''
    Questa funzione ha il compito di permettere permettere il collegamento con host esterni: fa partire un
    nameserver che verra' usato per registrare gli URI degli host esterni a cui ci si vuole collegare.
    '''
    print("Staring NS")
    try:
        
        Pyro4.naming.startNSloop()
    except socket.error:
        print("Server already started!!!")
        sys.exit(0)


def StartNameServerLoop():
    '''
     Questa funzione ha il compito di far partire il nameserver all'interno di un thread parallelo di tipo
    "demone" il quale si chiudera' automaticamente alla chiusura dell'applicazione
    '''
    
    NSThread = threading.Thread(target = startNameServer, args = [])
    NSThread.setDaemon(True)
    NSThread.start()
   
class Combo_Quit(QtGui.QWidget):
    '''
    Classe di tipo Qwidget che gestisce la gui per l'eliminazione di un Host dall'elenco
    @author Filippo Verucchi
    '''
    
    def __init__(self,main):
        
        super(Combo_Quit, self).__init__()
        self.ID = 0
        self.point_main = main
        self.__initUI()
        
    def __initUI(self):      
        layout = QtGui.QHBoxLayout(self)
        self.setLayout(layout)
        self.combo = QtGui.QComboBox(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        cmd_delete = QtGui.QPushButton("Elimina Host")
        cmd_delete.clicked.connect(self.__Ok_click)
        
        layout.addWidget(self.combo)
        layout.addWidget(cmd_delete)
        #combo.move(50, 50)        
        self.combo.activated[str].connect(self.__onActivated)        
         
        self.setGeometry(100,100,200,100)
        self.setWindowTitle('Elimina Host')
        self.update_host_list()
            
    def __onActivated(self, text):
        
        self.ID, spam = str(text).split(")")
        print(self.ID)   
    
    def __Ok_click(self):
        if (self.ID != 0 and self.ID !="<seleziona host>"):
            self.hide()
            print("finestra chiusa, vado dentro a elimina Host")
            self.point_main.elimina_host(self.ID,"Host eliminato da Utente")
            
    def update_host_list (self):
        '''
        Aggiorna l'elenco degli host connessi al nameserver
        '''
        print("Update list")
        #delete all items
        self.combo.clear()
        
        self.combo.addItem("<seleziona host>")
        for i in range(len(self.point_main.ui.host_w)):
            print("Nome host".format(self.point_main.ui.host_w[i].ID))
            if (self.point_main.ui.host_w[i].IP != "LOCAL"):
                host = str(str(self.point_main.ui.host_w[i].ID)+") " +self.point_main.ui.host_w[i].IP )
                self.combo.addItem(host)


        
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Main(QtGui.QMainWindow):
    '''
    Classi Main
    Qui viene inizializzato il programma
    @author Filippo Verucchi
    '''
    def __init__(self):
        
        
        self.__ID = 1
        
        Pyro4.config.HOST= "0.0.0.0"
        
        StartNameServerLoop()
        time.sleep(0.5)
        super(Main, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.freq = 0.05
        self.id_removed = []
        
        self.ui = INTRO_GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        
        self.Option = Option.Option(self)
        self.About = About.About()
        
        #MENU
        self.ui.actionAdd_Host.triggered.connect(self.__showDialog_in)
        self.ui.actionRemove_Host.triggered.connect(self.__showDialog_out)
        self.ui.actionQuit.triggered.connect(self.quit_prog)
        self.ui.actionGeneral_Options.triggered.connect(self.Option.show)
        self.ui.actionLoad_Configuration.triggered.connect(self.Option.load_settings)
        self.ui.actionSave_Configuration.triggered.connect(self.Option.save_settings)
        self.ui.actionAbout.triggered.connect(self.About.mostra)
        self.ui.actionDoc.triggered.connect(self._ShowDoc)
        
        print("host presenti {}".format(self.ui.gridLayout.count()))   
        
        self.combo = Combo_Quit(self)
        self.dialogbox = Qt.QErrorMessage()
        
        #Start Nameserver
    def quit_prog(self):
        '''
        Termina il programma
        '''
        self.Clear_list()
        print("Programma terminato con successo")
        
        sys.exit(0)    
    
    def _ShowDoc(self):
        webbrowser.open("fie:///html/index.html")
    
    def Clear_list (self):
        '''
        Vuota la lista degli host monitorati.
        Usata per caricare una nuova configurazione.
        '''
        print ("Vuota lista")
        n_host=len(self.ui.host_w)
        for i in range (n_host):
            if self.ui.host_w[i].ID !=0 and self.ui.host_w[i].ID not in self.id_removed:
                self.elimina_host(self.ui.host_w[i].ID, "NO_MSG")
    
    def set_Timer (self,timer):
        '''
        Setta la frequenza del timer di aggiornamento dati, lo setta a tutti gli host presenti nell'elenco
        @param timer numero in float che indica la frequenza di aggiornamento
        '''
        print("SetTimer = ",timer)
        self.freq = timer
        for i in range (len(self.ui.host_w)):
            self.ui.host_w[i].set_freq(self.freq)
            
    def __showDialog_in(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Inserire user@host:')
        
        passwd, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',"Inserire password per {}".format(text) , mode=2)
        
        
        if ok:
            if (text==""):
                print("Error NO IP")
                self.dialogbox.showMessage("Immettere un IP o un nome per il DNS")
            else:
                print("Creazione collegamento a {}".format(text))
                self.crea_conn(text,passwd)
                    
    def crea_conn (self,IP,passwd):
        '''
        Crea la connessione del programma a un server di monitoraggio
        @param IP Indirizzo o nome riconosciuto dal DNS del server    
        @param passwd Password d'accesso dell'utente 
        '''
        
        i = self.__ID
        try:        
            if (IP == ""):
                print (IP)
                raise Exception.MissingInputError
            
            print("IP=",IP)
            print("ID=",i)
            if (passwd == ""):
                passwd, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',"Inserire password per {}".format(IP) , mode=2)

            new_host = Host_Widget(IP,self,self.__ID,passwd)
            self.__ID+=1
            self.ui.host_w.append(new_host)
            self.ui.gridLayout.addWidget(new_host)    
            #print("host presenti {}".format(self.ui.gridLayout.count()))
        
        except AttributeError:
                self.dialogbox.showMessage("IP non corretto o Server {} non attivo".format(IP))
                self.__ID=i
                print("IP non corretto o Server {} non attivo".format(IP))
   
    
    def __showDialog_out(self):
        self.combo.update_host_list()
        
        self.combo.show()
    
    def elimina_host (self,ID,msg):
        '''
        Cancella dall'elenco un IP terminandone la connessione
        @param ID: Indirizzo del server da togliere
        @param msg: Messaggio da visualizzare tramite da DialogBox, con NO_MSG la finestra
        '''    
        print ("elimina host")
        if (ID==""):
                print("Errore")
        else:
                print("ID da cancellare {}".format(ID))
                i_id = -1
               
                for i in range(len(self.ui.host_w)):
                    
                    if (int(self.ui.host_w[i].ID)==int(ID)):
                        i_id = i
                print("indice -> {}".format(i_id))
                if (i_id!=-1):
                    widget = self.ui.gridLayout.itemAt(i_id)
                    widget.widget().setParent(None)
                    self.ui.host_w[i_id].local.Host_Cores.set_Stop()
                    self.ui.host_w[i_id].local.Host_Cores.closeSSHConnection()
                    self.ui.host_w.pop(i_id)
                    self.id_removed.append(ID)
                    
                    print(msg)
                    if (msg != "NO_MSG"):
                        self.dialogbox.showMessage(msg)
                        print("IP removed {}".format(ID))
                        print("Tolto 1 IP, rimanenti host ={}".format(self.ui.gridLayout.count()))
                    
                else:
                    print("ID non trovato")
    
   
    def closeEvent(self,event):
        self.quit_prog()
        #time.sleep(3)
        sys.exit(0)
    


def main():
    parser = argparse.ArgumentParser(description='Aggiunta di argomenti da startUp')    
    parser.add_argument("-a","--address",nargs="+", help="Imposta gli IP da caricare all'esecuzione del programma")
    parser.add_argument("-c","--config",help="Imposta il file di configurazione da caricare all'avvio")
    parser.add_argument("-t","--timer",help="Imposta il timer di aggiornamento dei valori")
    args = parser.parse_args()
    print(args.address)
    print(args.config)
    
    
    print("CIAO")
    
    app = QtGui.QApplication(sys.argv)
    intro = Main()
    
    #usiamo gli argomenti
    if (args.address != None):
        lista_IP = args.address
        for i in range (len(lista_IP)):
            intro.crea_conn(lista_IP[i],"")
    #NEED LOAD A CFGfile
    if (args.config != None):
        cfg = args.config
        intro.Option.load_settings(cfg)
    intro.show()
    
    if (args.timer != None):
        timer = args.timer
        intro.set_Timer(timer)
        
    sys.exit(app.exec_())
if __name__ == '__main__':
    '''
    @mainpage asd
    '''
    main()

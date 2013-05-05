'''
Created on 09/apr/2013

@author: phil
'''

from PyQt4 import QtGui, Qt
import INTRO_GUI
import sys
import Option
from Host_Widget import Host_Widget
    
class Combo_Quit(QtGui.QWidget):
    
    def __init__(self,main):
        super(Combo_Quit, self).__init__()
        self.IP = 0
        self.point_main = main
        self.initUI()
        
    def initUI(self):      
        layout = QtGui.QHBoxLayout(self)
        self.setLayout(layout)
        self.combo = QtGui.QComboBox(self)
        
        cmd_delete = QtGui.QPushButton("Elimina Host")
        cmd_delete.clicked.connect(self.Ok_click)
        
        layout.addWidget(self.combo)
        layout.addWidget(cmd_delete)
        #combo.move(50, 50)        
        self.combo.activated[str].connect(self.onActivated)        
         
        self.setGeometry(100,100,200,100)
        self.setWindowTitle('Elimina Host')
        self.update_host_list()
            
    def onActivated(self, text):
      
        self.IP=text
        print(self.IP)   
    
    def Ok_click(self):
        if (self.IP != 0 and self.IP !="<seleziona host>"):
            self.hide()
            print("finestra chiusa, vado dentro a elimina Host")
            self.point_main.elimina_host(self.IP,"Host eliminato da Utente")
            
            
    def update_host_list (self):
        
        #delete all items
        self.combo.clear()
        
        self.combo.addItem("<seleziona host>")
        for i in range(len(self.point_main.ui.host_w)):
            print("Nome host".format(self.point_main.ui.host_w[i].IP))
            if (self.point_main.ui.host_w[i].IP != "LOCAL"):
                self.combo.addItem(self.point_main.ui.host_w[i].IP)
        
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Main(QtGui.QMainWindow):
    def __init__(self):
        """
        Costruttore della classe MainWindow.
     
        """
        super(Main, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.freq = 0.05
        self.ui = INTRO_GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        
        self.Option = Option.Option(self)
        
        
        self.ui.actionAdd_Host.triggered.connect(self.showDialog_in)
        self.ui.actionRemove_Host.triggered.connect(self.showDialog_out)
        self.ui.actionQuit.triggered.connect(self.quit_prog)
        self.ui.actionGeneral_Options.triggered.connect(self.Option.show)
        self.ui.actionLoad_Configuration.triggered.connect(self.Option.load_settings)
        self.ui.actionSave_Configuration.triggered.connect(self.Option.save_settings)
        print("host presenti {}".format(self.ui.gridLayout.count()))   
        
        self.combo = Combo_Quit(self)
        self.dialogbox = Qt.QErrorMessage()
        #self.freq
        
            
    def quit_prog (self):
        print("Programma terminato con successo")
        sys.exit(0)  
    
    '''
    Setta la frequenza del timer di aggiornamento dati, lo setta a tutti gli host presenti nell'elenco
    '''
    def set_Timer (self,timer):
        
        print("SetTimer = ",timer)
        self.freq = timer
        for i in range (len(self.ui.host_w)):
            self.ui.host_w[i].set_freq(self.freq)
     
    def showDialog_in(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Ip da aggungere:')
        
        if ok:
            if (text==""):
                print("Errore")
                self.dialogbox.showMessage("Immettere un IP o un nome per il DNS")
            else:
                print("Creazione collegamento a {}".format(text))
                self.crea_conn(text)
                
                
    def crea_conn (self,IP):       
            try:
                if (IP == ""):
                    raise Exception.MissingInputError
                print("IP=",IP)
                new_host = Host_Widget(IP,self)
                self.ui.host_w.append(new_host)
                self.ui.gridLayout.addWidget(new_host)    
                print("host presenti {}".format(self.ui.gridLayout.count()))   
            except AttributeError:
                self.dialogbox.showMessage("IP non corretto o Server {} non attivo".format(IP))
                print("Errore")
    def showDialog_out(self):
        self.combo.update_host_list()
        
        self.combo.show()
    def elimina_host (self,IP,msg):
        
        self.dialogbox.showMessage(msg)
        if (IP==""):
                print("Errore")
        else:
                print("indirizzo da cancellare {}".format(IP))
                i_ip = -1
                for i in range(len(self.ui.host_w)):
                    if (self.ui.host_w[i].IP==IP):
                        i_ip = i
                
                if (i_ip!=-1):
                    
                    widget = self.ui.gridLayout.itemAt(i_ip)
                    
                    widget.widget().setParent(None)
                    self.ui.host_w[i_ip].local.My_Host.set_Stop()
                    
                    
                    self.ui.host_w.pop(i_ip)
                    
                    
                    self.dialogbox.show()
                    print(msg)
                    
                    print("IP removed {}".format(IP))
                    print("Tolto 1 IP, rimanenti host ={}".format(self.ui.gridLayout.count()))
                    
                else:
                    print("IP non trovato")
    
   
    def closeEvent(self,event):    
        sys.exit(0)
        
    
def main():
    print("CIAO")
    
    app = QtGui.QApplication(sys.argv)
    intro = Main()
    
    #NEED LOAD A CFGfile
    intro.show()
    
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
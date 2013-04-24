'''
Created on 09/apr/2013

@author: phil
'''

from PyQt4 import QtCore, QtGui, Qt
import INTRO_GUI
import sys
import LocalHost



class Host_Widget (QtGui.QPushButton):
    
    def __init__(self,IP,Main):
        super(Host_Widget, self).__init__()
        
        
        self.Main = Main
        self.IP=IP
        self.ping_True = False
        self.local = LocalHost.LocalHost(self.IP,0.1)
        
       
        self.clicked.connect(self.show_window) #BISOGNA CONNETTERLO ALLE FINESTRE! O PERLOMENO LEGGERE I DATI DA REMOTO PER CREARE OGNI VOLTA FINESTRE DIVERSE
        self.local.My_Host.valore_generico.connect(self.show_generic_load)
        self.carico = 0
        
        self.local.My_Host.connection_lost.connect(self.Main.elimina_host)
        self.local.My_Host.connection_ok.connect(self.Ping_ON)
        
    def Ping_ON (self):
        
        self.ping_True= True
        
    def Ping_Off (self):
        self.ping_True = False
        
    def paintEvent(self, event):
        
       
        qp = QtGui.QPainter()
        qp.begin(self)
        #qp.setRenderHint(QtGui.QPainter.Antialiasing)
        #qp.setPen(QtCore.Qt.green)
        #qp.drawText(50,50,"{}".format(percent))
       
        if (self.ping_True==False and self.IP != "LOCAL"):
            qp.setBrush(Qt.QBrush(QtCore.Qt.gray))
        elif self.carico < 10:
            qp.setBrush(Qt.QBrush(QtCore.Qt.green))
        elif self.carico <20:
            qp.setBrush(Qt.QBrush(QtCore.Qt.yellow))
        else:
            qp.setBrush(Qt.QBrush(QtCore.Qt.red))
  
        qp.drawRect(0,0,self.width(),self.height())
        qp.setPen(QtCore.Qt.black)
        qp.drawText(20,20, "{} - {}".format(self.IP,self.carico))
        
    def show_window(self):
       
        self.local.start_thread()
        self.local.My_Host.set_Start()
        self.local.show()
        
    def show_generic_load (self,carico):
    
        self.carico= carico
        self.repaint()
        #print(("Carico {}".format(carico)))
    
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
        self.ui = INTRO_GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd_Host.triggered.connect(self.showDialog_in)
        self.ui.actionRemove_Host.triggered.connect(self.showDialog_out)
        self.ui.actionQuit.triggered.connect(self.quit_prog)
        print("host presenti {}".format(self.ui.gridLayout.count()))   
        self.combo = Combo_Quit(self)
        self.dialogbox = Qt.QErrorMessage()
        
    def quit_prog (self):
        print("Programma terminato")
        sys.exit(0)   
    def showDialog_in(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Ip da aggungere:')
        
        if ok:
            if (text==""):
                print("Errore")
                self.dialogbox.showMessage("Immettere un IP o un nome per il DNS")
            else:
                print("IP aggiunto {}".format(text))
               
                try:
                    new_host = Host_Widget(text,self)
                    self.ui.host_w.append(new_host)
                    self.ui.gridLayout.addWidget(new_host)    
                    print("host presenti {}".format(self.ui.gridLayout.count()))   
                except AttributeError:
                    self.dialogbox.showMessage("Errore! IP non corretto")
                    print("Errore! IP non corretto")
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

        
def main():
    print("CIAO")
    
    
    app = QtGui.QApplication(sys.argv)
    intro = Main()
    intro.show()
    
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
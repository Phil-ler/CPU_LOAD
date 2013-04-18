'''
Created on 09/apr/2013

@author: phil
'''

from PyQt4 import QtCore, QtGui, Qt
import INTRO_GUI
import sys
import LocalHost

class Host_Widget (QtGui.QPushButton):
    
    def __init__(self,IP):
        super(Host_Widget, self).__init__()
     
        self.IP=IP
        self.local = LocalHost.LocalHost(self.IP,0.1)
        
        #vbox = QtGui.QVBoxLayout()
        #self.setLayout(vbox)
        #cmd_Host = QtGui.QPushButton(self.IP)
        self.clicked.connect(self.show_window) #BISOGNA CONNETTERLO ALLE FINESTRE! O PERLOMENO LEGGERE I DATI DA REMOTO PER CREARE OGNI VOLTA FINESTRE DIVERSE
        self.local.My_Host.valore_generico.connect(self.show_generic_load)
        self.carico = 0
        #self.local._thread.start()
        
        
    '''    cmd_go = QtGui.QPushButton("Start/Stop")
        cmd_go.setObjectName("cmd_go")
        cmd_go.
        self.start_stop = False
    '''
    def paintEvent(self, event):
        
       
        qp = QtGui.QPainter()
        qp.begin(self)
        #qp.setRenderHint(QtGui.QPainter.Antialiasing)
        #qp.setPen(QtCore.Qt.green)
        #qp.drawText(50,50,"{}".format(percent))
        qp.setPen(QtCore.Qt.black)
        if self.carico < 10:
            qp.setBrush(Qt.QBrush(QtCore.Qt.green))
        elif self.carico <20:
            qp.setBrush(Qt.QBrush(QtCore.Qt.yellow))
        else:
            qp.setBrush(Qt.QBrush(QtCore.Qt.red))
        
        qp.drawRect(0,0,self.width(),self.height())
        qp.drawText(20,20, "{} - {}".format(self.IP,self.carico))
        
    
    def show_window(self):
       
        self.local.start_thread()
        self.local.show()
        
    def show_generic_load (self,carico):
    
        self.carico= carico
        self.repaint()
        #print(("Carico {}".format(carico)))
    
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
        print("host presenti {}".format(self.ui.gridLayout.count()))   
        
    def showDialog_in(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Ip da aggungere:')
        
        if ok:
            if (text==""):
                print("Errore")
            else:
                print("IP aggiunto {}".format(text))
               
                new_host = Host_Widget(text)
                self.ui.host_w.append(new_host)
                self.ui.gridLayout.addWidget(new_host)    
                print("host presenti {}".format(self.ui.gridLayout.count()))   
    def showDialog_out(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'IP da togliere:')
        
        if ok:
            if (text==""):
                print("Errore")
            # elif (text=="localhost" or text=="127.0.0.1"):
            #     print("IDIOTA")
            else:
                i_ip = -1
                for i in range(len(self.ui.host_w)):
                    if (self.ui.host_w[i].IP==text):
                        i_ip = i
                
                if (i_ip!=-1):
                    widget = self.ui.gridLayout.itemAt(i_ip)
                    widget.widget().setParent(None)
                    self.ui.host_w.pop(i_ip)
                    print("IP removed {}".format(text))
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
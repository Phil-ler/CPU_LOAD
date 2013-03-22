'''

Created on 20/mar/2013

@author: phil
'''
import psutil
from Host import Host
from PyQt4 import QtCore,QtGui
import CPU_GUI
import sys


class MainWindow(QtGui.QMainWindow):
    """
    Classe della finestra principale
    
    """
    def read(self):
        #print("Leggo")
        carico=self.My_Host.Run(0.1)        
        #self.ui.lcdNumber.display(carico[0])
        for i in range (self.num_Host):
            self.ui.lcd[i].display(carico[i])
        
        
    def avvio(self):
        print("asd")
        if self.timer.isActive(): 
            self.timer.stop()
        else:
            self.timer.start() 
        
    def __init__(self):
        """
        Costruttore della classe MainWindow.
        
        """
        super(MainWindow, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CPU_GUI.Ui_frmHost()
        self.ui.setupUi(self.centralWidget())
        self.timer = QtCore.QTimer()
        self.timer.setInterval(0)
        self.timer.timeout.connect(self.read)
        #self.ui.pushButton.clicked.connect(self.avvio)
        self.num_Host = psutil.NUM_CPUS
        self.My_Host = Host(self.num_Host)
        #self.setCentralWidget(self.ui)
        self.avvio()
       



def main():
    print("CIAO")
    
    app = QtGui.QApplication(sys.argv)

    my_mainWindow = MainWindow()
    my_mainWindow.show()

    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

import LocalHost
from PyQt4 import QtCore, QtGui, Qt

'''
Created on 26/apr/2013

@author: phil
'''
class Host_Widget (QtGui.QPushButton):
    
    def __init__(self,IP,Main):
        super(Host_Widget, self).__init__()
        
        
        self.Main = Main
        self.IP=IP
        self.timer = self.Main.freq
        self.ping_True = False
        self.local = LocalHost.LocalHost(self.IP,self.timer)
        
       
        self.clicked.connect(self.show_window)
        self.local.My_Host.valore_generico.connect(self.show_generic_load)
        self.carico = 0
        
        self.local.My_Host.connection_lost.connect(self.Main.elimina_host)
        self.local.My_Host.connection_ok.connect(self.Ping_ON)
        
    def set_freq (self,freq):
        self.timer = freq
        self.local.set_timer(self.timer)
    
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
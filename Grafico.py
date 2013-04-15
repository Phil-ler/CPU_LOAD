'''
Created on 04/apr/2013

@author: phil
'''
from PyQt4 import QtCore, QtGui, Qt
import Core
#from test.test_bufio import lengths
class Grafico(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Grafico, self).__init__()
        self.text ="CIAO"
        self.coda = []
        
    def setNextPoint (self,punto):
        self.coda=punto
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        #self.drawPoint(event, qp)
        self.drawGrid(event, qp)
        qp.save()
        qp.translate(0,self.height())
        qp.scale(self.width()/Core.Core.limite_nodi-1,-self.height()/101)
        self.drawline(event,qp)
        qp.restore()
        qp.end()
    
    def drawGrid(self,event,qp):
        
        qp.setBrush(Qt.QBrush(QtCore.Qt.black)) #"#c56c00"
        qp.drawRect(0,0,self.width(),self.height())
        qp.setPen(QtCore.Qt.white)
        qp.drawText(0,self.height(),"0")
        qp.drawText(0,self.height()*0.5,"50")
        qp.drawText(0,self.height()*0.75,"25")
        qp.drawText(0,self.height()*0.25,"75")
        qp.drawText(0,self.height()*0.05,"100")
        
        
    
    def drawline (self,event,qp):
        y_init = self.coda[0]
        x_init= -1
        #print("altezza= {}".format(self.height()))
        #print("coda = {}".format(self.coda))
        for i in range (len(self.coda)):
           
            if (self.coda[i]<50):
                colore=QtCore.Qt.green
            elif (self.coda[i]<80):
                colore=QtCore.Qt.yellow
            else: colore=QtCore.Qt.red
            #pen = QtGui.QPen(colore, 2, QtCore.Qt.SolidLine)
            pen = QtGui.QPen(colore)
            qp.setPen(pen)
            qp.drawLine(x_init,y_init,x_init+1,self.coda[i])
            x_init, y_init= x_init+1, self.coda[i]
       
        
    '''
    Classe di Test del widget
    '''
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(0, 0, 255)) #red green blue
        qp.setFont(QtGui.QFont('Decorative', 50))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 
'''
Created on 04/apr/2013

@author: phil
'''
from PyQt4 import QtCore, QtGui, Qt
import Core
from test.test_bufio import lengths
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
        self.limite_coda = 10
        self.last_N = -1

    def setNextPoint (self,punto):
        self.coda=punto
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        #self.drawPoint(event, qp)
        self.drawGrid(event, qp)
        self.drawline(event,qp)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.end()
    
    def drawGrid(self,event,qp):
        
        qp.setBrush(Qt.QBrush(QtCore.Qt.gray)) #"#c56c00"
        qp.drawRect(0,0, 1000, 500)
    
    def drawline (self,event,qp):
        
        if (self.last_N !=-1):
            y_init= self.last_N
        
        else :
            y_init = 0
        x_init=0
        for i in range (len(self.coda)):
           
            if (self.coda[i]<20):
                colore=QtCore.Qt.green
            elif (self.coda[i]<40):
                colore=QtCore.Qt.yellow
            else: colore=QtCore.Qt.red
            pen = QtGui.QPen(colore, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(x_init,y_init,10+x_init,self.coda[i]+10)
            x_init, y_init= x_init+10, self.coda[i]+10
        if (i > self.limite_coda):
            self.coda.pop(0)
            self.last_N=self.coda[0]+10
    def drawPoint (self,event,qp):
        
        qp.setPen(QtCore.Qt.red)
        #size = self.size()  
        for i in range (100):
            qp.drawPoint(100,100+i)
    
    '''
    Classe di Test del widget
    '''
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(0, 0, 255)) #red green blue
        qp.setFont(QtGui.QFont('Decorative', 50))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 
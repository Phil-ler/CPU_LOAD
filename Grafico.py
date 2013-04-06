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
        mult =100
        y_init = self.coda[0] + mult 
        x_init= 0
        for i in range (len(self.coda)):
           
            if (self.coda[i]<20):
                colore=QtCore.Qt.green
            elif (self.coda[i]<40):
                colore=QtCore.Qt.yellow
            else: colore=QtCore.Qt.red
            pen = QtGui.QPen(colore, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(x_init,y_init,mult/5+x_init,self.coda[i]+mult)
            x_init, y_init= x_init+mult/5, self.coda[i]+mult
       
        
    '''
    Classe di Test del widget
    '''
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(0, 0, 255)) #red green blue
        qp.setFont(QtGui.QFont('Decorative', 50))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 
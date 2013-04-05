'''
Created on 04/apr/2013

@author: phil
'''
from PyQt4 import QtCore, QtGui, Qt
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
        self.contatore = 0
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRect(event, qp)
        self.drawPoint(event, qp)
        self.drawline(event,qp)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.end()
    
    def drawRect(self,event,qp):
        
        qp.setBrush(Qt.QBrush("#c56c00"))
        qp.drawRect(0,0, 700, 300)
    
    def drawline (self,event,qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20+self.contatore, 40, 250+self.contatore, 40)
        self.contatore+=1
    
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
'''
Created on 04/apr/2013

@author: phil
'''
from PyQt4 import QtCore, QtGui, Qt
import Core
#from test.test_bufio import lengths
class Grafico(QtGui.QWidget):
    '''
    Widget dedicato al disegno del grafico del carico di un singolo core
    '''


    def __init__(self):
        super(Grafico, self).__init__()
       
        self.__coda = []
   
    def setNextPoint (self,punto):
        '''
    Setta la lista aggiornata dentro la variabile interna, dedicata al disegno del grafico
    '''
        self.__coda=punto
        
    def paintEvent(self, event):
        '''
    Paint event della classe grafico
    '''
    
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
        '''
    Disegna la griglia di fondo del grafico
    '''
        qp.setBrush(Qt.QBrush(QtCore.Qt.black)) #"#c56c00"
        qp.drawRect(0,0,self.width(),self.height())
        qp.setPen(QtCore.Qt.white)
        qp.drawText(0,self.height(),"0")
        qp.drawText(0,self.height()*0.5,"50")
        qp.drawText(0,self.height()*0.75,"25")
        qp.drawText(0,self.height()*0.25,"75")
        qp.drawText(0,self.height()*0.05,"100")
        
        '''
    Disegna l'andamento del grafico
    @param qp: QPainter
    '''
    def drawline (self,event,qp):
        y_init = self.__coda[0]
        x_init= -1
        #print("altezza= {}".format(self.height()))
        #print("__coda = {}".format(self.__coda))
        for i in range (len(self.__coda)):
           
            if (self.__coda[i]<50):
                colore=QtCore.Qt.green
            elif (self.__coda[i]<80):
                colore=QtCore.Qt.yellow
            else: colore=QtCore.Qt.red
            #pen = QtGui.QPen(colore, 2, QtCore.Qt.SolidLine)
            pen = QtGui.QPen(colore)
            qp.setPen(pen)
            qp.drawLine(x_init,y_init,x_init+1,self.__coda[i])
            x_init, y_init= x_init+1, self.__coda[i]
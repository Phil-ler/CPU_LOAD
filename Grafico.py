'''
Widget che disegna a video l'andamento del carico della CPU designata
@author: Filippo Verucchi
'''
from PyQt4 import QtCore, QtGui, Qt
import Core
#from test.test_bufio import lengths
class Grafico(QtGui.QWidget):
    '''
    Widget dedicato al disegno del grafico del carico di un singolo core
    Viene designato un grafico tempo-carico
    '''


    def __init__(self):
        super(Grafico, self).__init__()
       
        self.__coda = []
   
    def setNextPoint (self,punto):
        '''
        Setta la lista aggiornata dentro la variabile interna, dedicata al disegno del grafico
        @param prossimo punto da disegnare
        '''
        self.__coda=punto
        
    def paintEvent(self, event):
        '''
        Paint event della classe grafico
        Chiamato da solo ogni volta che viene disegnato qualcosa
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
        Vengono mostrare 4 rette mostranti i valori del 25%, 50%, 75%, 100% del carico
        @param event
        @param Oggetto QPainter
        '''
        qp.setBrush(Qt.QBrush(QtCore.Qt.black)) #"#c56c00"
        qp.drawRect(0,0,self.width(),self.height())
        qp.setPen(QtCore.Qt.white)
        qp.drawText(0,self.height(),"0")
        qp.drawText(0,self.height()*0.5,"50")
        qp.drawText(0,self.height()*0.75,"25")
        qp.drawText(0,self.height()*0.25,"75")
        qp.drawText(0,self.height()*0.05,"100")
        pen = QtGui.QPen(QtCore.Qt.cyan, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        #qp.setPen(QtCore.Qt.DashDotLine)
        qp.drawLine(0,self.height()*0.5,self.width(),self.height()*0.5)
        qp.drawLine(0,self.height()*0.75,self.width(),self.height()*0.75)
        qp.drawLine(0,self.height()*0.25,self.width(),self.height()*0.25)
        qp.drawLine(0,self.height()*0.05,self.width(),self.height()*0.05)
        
       
    def drawline (self,event,qp):
       
        '''
        Disegna l'andamento del grafico
        @param event
        @param qp: QPainter
        '''
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
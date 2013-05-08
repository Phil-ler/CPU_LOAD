'''
Created on 20/mar/2013

@author: phil
'''
from PyQt4 import QtCore,QtGui
import CORE_GUI



class Core(QtGui.QMainWindow):
    '''
    Classe che identifica un singolo Core della CPU
    '''
    limite_nodi= 50

    def __init__(self,n):
        '''
        Constructor
        '''
        super(Core, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CORE_GUI.Ui_frm_core()
        self.ui.setupUi(self.centralWidget())
        #self.limite_nodi = limite_nodi
        
        self.number=n
        self.perc_carico=[] #percentuale del carico
        self.colore="grigio" #colore del bollino
        self.media=0    #media del carico delle ultime N letture
        #----------------------------------------------------------
        self.label_core="Core #{}".format(self.number+1)
        self.ui.lbl_core.setText(self.label_core)
        self.setWindowTitle(self.label_core)
    '''
    Dato il carico, mette il suo valore in coda per essere disegnato
    @param carico: Carico attuale del core
    '''
    def load (self,carico):
               
        if (carico < 0): self.colore="grigio"  
        elif (carico < 60): self.colore="verde"
        elif (carico < 80): self.colore="giallo"
        else: self.colore="rosso"
        self.ui.lbl_carico.setText("{}".format(carico))
        self.perc_carico.append(carico)
    
    '''
    segnala al grafico il prossimo punto da disegnare, passando anche i precedenti
    '''        
    def traccia (self):
        
        if (len(self.perc_carico) >= self.limite_nodi):
            coda_da_disegnare = self.perc_carico[len(self.perc_carico)-self.limite_nodi:len(self.perc_carico)]
            self.ui.grafico.setNextPoint(coda_da_disegnare)
        
        else :
            self.ui.grafico.setNextPoint(self.perc_carico)
        
        self.ui.grafico.repaint()
        #print ("Core #=",self.number," carico= ",self.perc_carico," colore= ",self.colore)
        
        
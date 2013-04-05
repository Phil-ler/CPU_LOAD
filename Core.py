'''
Created on 20/mar/2013

@author: phil
'''
from PyQt4 import QtCore,QtGui
import CORE_GUI


class Core(QtGui.QMainWindow):
    '''
    classdocs
    '''
    

    def __init__(self,n):
        '''
        Constructor
        '''
        super(Core, self).__init__()
        self.setCentralWidget(QtGui.QWidget(self))
        self.ui = CORE_GUI.Ui_frm_core()
        self.ui.setupUi(self.centralWidget())
        
        
        self.number=n
        self.perc_carico=[] #percentuale del carico
        self.colore="grigio" #colore del bollino
        self.media=0    #media del carico delle ultime N letture
        #----------------------------------------------------------
        self.label_core="Core #{}".format(self.number+1)
        self.ui.lbl_core.setText(self.label_core)
        self.setWindowTitle(self.label_core)
    def load (self,carico):
        ''' 
        
        '''
        
        if (carico < 0): self.colore="grigio"  
        elif (carico < 60): self.colore="verde"
        elif (carico < 80): self.colore="giallo"
        else: self.colore="rosso"
        self.ui.lbl_carico.setText("{}".format(carico))
        self.perc_carico.append(carico)
    
    def traccia (self):
        self.ui.grafico.setNextPoint(self.perc_carico)
        self.ui.grafico.repaint()
        #print ("Core #=",self.number," carico= ",self.perc_carico," colore= ",self.colore)
        
        
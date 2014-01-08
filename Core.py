'''
Modulo Core
Contiene le informazioni di un singolo Core della CPU e usa i valori contenuti per disegnare il grafico inerente
@author: Filippo Verucchi
'''
from PyQt4 import QtCore,QtGui
import CORE_GUI
from test import test_signal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class Core(QtGui.QMainWindow):
    '''
    Classe che identifica un singolo Core della CPU
    @author Filippo Verucchi
    '''
    limite_nodi= 50
    S_Test =QtCore.pyqtSignal(float)
    def __init__(self,n):
       
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
        #TEXT AREA
        if (self.number== -1):
            self.doubleSpinBox = QtGui.QDoubleSpinBox()
            self.doubleSpinBox.setGeometry(QtCore.QRect(20, 40, 64, 33))
            self.doubleSpinBox.setMinimum(-2)
            self.doubleSpinBox.setMaximum(105)
            self.doubleSpinBox.setSingleStep(1)
            self.doubleSpinBox.setProperty("value", 1)
            self.doubleSpinBox.setObjectName(_fromUtf8("self.doubleSpinBox2"))
            self.ui.verticalLayout.addWidget(self.doubleSpinBox) 
            cmd_disegna = QtGui.QPushButton("Disegna")
            cmd_disegna.clicked.connect(self.__disegna_test)
            self.ui.verticalLayout.addWidget(cmd_disegna)
            cmd_scala = QtGui.QPushButton("Test")
            cmd_scala.clicked.connect(self.__scala_test)
            self.ui.verticalLayout.addWidget(cmd_scala)
    
    def __scala_test(self):
            
            cont = 20
            j=1
            val = 0
            for i in range(13):
                val+=j*cont
                self.load(val)
                self.traccia()
                self.S_Test.emit(val)
                if (val == 120):
                    j = -1
    def __disegna_test(self):
        
        val =self.doubleSpinBox.value()
        print(val)
        self.load(val)
        self.traccia()
        self.S_Test.emit(val)        
                    
   
    def load (self,carico):
        '''
        Dato il carico, mette il suo valore in coda per essere disegnato
        @param carico: Carico attuale del core
        '''      
        if (carico < 0): self.colore="grigio"  
        elif (carico < 60): self.colore="verde"
        elif (carico < 80): self.colore="giallo"
        else: self.colore="rosso"
        self.ui.lbl_carico.setText("{}".format(carico))
        self.perc_carico.append(carico)
    
           
    def traccia (self):
        '''
        Segnala al grafico il prossimo punto da disegnare, passando anche i precedenti
        
        ''' 
        if (len(self.perc_carico) >= self.limite_nodi):
            coda_da_disegnare = self.perc_carico[len(self.perc_carico)-self.limite_nodi:len(self.perc_carico)]
            self.ui.grafico.setNextPoint(coda_da_disegnare)
        
        else :
            self.ui.grafico.setNextPoint(self.perc_carico)
        self.ui.grafico.repaint()
        #print ("Core #=",self.number," carico= ",self.perc_carico," colore= ",self.colore)
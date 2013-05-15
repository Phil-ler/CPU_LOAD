'''
Created on 10/mag/2013

@author: phil
'''
import unittest
from Analizzatore import Analizzatore
import sys
from PyQt4 import QtGui, Qt
import Core 

class Test(unittest.TestCase):
    
        
    def setUp(self):
        
        
        self.A = Analizzatore()
        self.list = []
        self.media = [self.A.get_n_core()]
        for i in range (self.A.get_n_core()):
            self.media.append(0)
   
    '''
    Testa il carico della CPU a PC scarico, effettua 50 letture di carico, e se la media di carico di un Core è superiore alla soglia di 0.2 genera un errore
    '''
    def test_lower_load(self):
        print("Test di lettura a macchina scarica, chiudere tutti i programmi")
        input("Premere un tasto per continuare")
       
        print("Lettura in corso")
        for i in range (50):
            print("."*(i+1))
            carico = self.A.get_cores_values()
            self.list.append(carico)
            
        for i in range (self.A.get_n_core()):
            for j in range (50):
                self.media[i]=self.list[j][i]
                
        for i in range (self.A.get_n_core()):
            self.media[i]/=50
            print(self.media[i])
            self.assertLessEqual(self.media[i], 0.2, "Test Fallito! Computer in uso!")
    
    def check_data(self,val):
        print("Valore preso dal segnale",val)
        self.assertGreaterEqual(val, 0.00, "Valore oltre la scala inferiore")
        self.assertLessEqual(val, 100.00, "Valore oltre la scala superiore")
    '''
    Viene creato un core fittizio dove è possibile inserire manualmente dei valori che verranno disegnati sul grafico
    '''
    def test_graph(self):
        
        
        self.app = QtGui.QApplication(sys.argv)
        
        self.C = Core.Core(-1)
        self.C.S_Test.connect(self.check_data)
        self.C.load(0)
        self.C.traccia()
        self.C.show()
        print("CIAO GRAPH")
        
        sys.exit(self.app.exec_())
    
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
        
        self.A1 = Analizzatore()
        self.list = []
        self.media = [self.A1.get_n_core()]
        for i in range (self.A1.get_n_core()):
            self.media.append(0)
            
        self.app = QtGui.QApplication(sys.argv)

        self.C = Core.Core(-1)
        self.C.S_Test.connect(self.check_data)
   
    def testgraph(self):
        '''
        Viene creato un core fittizio dove è possibile inserire manualmente dei valori che verranno disegnati sul grafico
        
        '''
            
        
        self.C.load(0)
        self.C.traccia()
        self.C.show()
        #print("CIAO GRAPH")
        self.app.exec_()
    
        
    def tearDown(self):
        
        del self.A1
        del self.C
        del self.app
        
    def test_one_read(self):
        '''
        Effettua una lettura singola per verificare di leggere i valori corretti
        
        '''
        print ("Verrà effettuata una singola lettura, il valore non deve uscire dal range")
        input ("Premere invio per continuare")
        read = self.A1.get_generic(0)
        self.assertGreaterEqual(read,0,"Errore di lettura")
    
    def test_lower_load(self):
        '''
        Testa il carico della CPU a PC scarico, effettua 50 letture di carico, e se la media di carico di un Core è superiore alla soglia di 0.2 genera un errore
        
        '''
        print("Test di lettura a macchina scarica, chiudere tutti i programmi")
        input("Premere invio per continuare")
       
        print("Lettura in corso")
        for i in range (50):
            print("."*(i+1))
            carico = self.A1.get_cores_values()
            self.list.append(carico)
            
        for i in range (self.A1.get_n_core()):
            for j in range (50):
                self.media[i]=self.list[j][i]
                
        for i in range (self.A1.get_n_core()):
            self.media[i]/=50
            print(self.media[i])
            self.assertLessEqual(self.media[i], 0.2, "Test Fallito! Computer in uso!")
   
    
   
    def check_data(self,val):
        '''
        Controlla il valore preso dal segnale
        se esce dal range di valori concessi, solleva un eccezione
        @param val: valore da analizzare
        '''
        print("Valore preso dal segnale",val)
        self.assertGreaterEqual(val, 0.00, "Valore oltre la scala inferiore")
        self.assertLessEqual(val, 100.00, "Valore oltre la scala superiore")
        
   
    
   
       
      
   
        
        

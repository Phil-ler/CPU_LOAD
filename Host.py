'''
Created on 20/mar/2013

@author: phil
'''
from Core import *
import psutil
class Host():
    '''
    classdocs
    '''
    

    def __init__(self,Num_Cores):
        '''
        Constructor
        '''
        self.Num_Cores=Num_Cores
        self.core = []
        
        for i in range(self.Num_Cores):
            self.core.append(Core(i))
            print("Core creato n°",i)
            
    def fill (self,percent):
        for i in range(self.Num_Cores):
            #print ("Carico del processore ",percent[c])
            self.core[i].load(percent[i])
                            
    def Run(self,timer):
        #while(True):
            percent=psutil.cpu_percent(interval=timer, percpu=True)
            print(percent)
            self.fill(percent)
        
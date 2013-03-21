'''
Created on 20/mar/2013

@author: phil
'''
import Core
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
            self.core.append(Core.Core(10))
            print("Core creato n°",i)
            
    def fill (self,percent):
        for c in range(self.Num_Cores):
            print("Ciao",c) 
            
                            
    def Run(self,timer):
        #while(True):
            percent=psutil.cpu_percent(interval=timer, percpu=True)
            print(percent)
            self.fill(percent)
        
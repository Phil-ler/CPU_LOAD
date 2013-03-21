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
      #--------------------------------------------  
    def find_comma(self,start):
        print("start= ",start)
        i=start
        while i!=',':
            i=i+1
        return i
            
    def fill (self,percent):
        
        for i in range(1,self.Num_Cores):
                  
            comma=self.find_comma(i)
            print("la virgola è ",comma)
            i=comma+1
        
        
            
          
                
                
    def Run(self,timer):
        #while(True):
            percent=psutil.cpu_percent(interval=timer, percpu=True)
            print(percent)
            self.fill(percent)
        
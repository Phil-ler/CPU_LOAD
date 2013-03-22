'''
Created on 20/mar/2013

@author: phil
'''

class Core(object):
    '''
    classdocs
    '''
    

    def __init__(self,n):
        '''
        Constructor
        '''
        self.number=n
        self.perc_carico=[] #percentuale del carico
        self.colore="grigio" #colore del bollino
        self.media=0    #media del carico delle ultime N letture
       
    def load (self,carico):
        ''' 
        
        '''
        if (carico < 0): self.colore="grigio"  
        elif (carico < 60): self.colore="verde"
        elif (carico < 80): self.colore="giallo"
        else: self.colore="rosso"
        
        self.perc_carico=carico
       # print ("Core #=",self.number," carico= ",self.perc_carico," colore= ",self.colore)
        
        
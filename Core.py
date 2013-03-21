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
        self.perc_carico=None #percentuale del carico
        self.colore="grigio" #colore del bollino
        self.media=0    #media del carico delle ultime N letture
        self.n=n 
       
        
        
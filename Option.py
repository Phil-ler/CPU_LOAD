# -*- coding: iso-8859-15 -*-
'''
Created on 29/apr/2013

@author: phil
'''
from PyQt4 import QtGui, Qt
import OPTION_GUI
import configparser
class Option(QtGui.QDialog):
   
    '''
    Classe Option
    
    Finestra di dialogo che gestisce le impostazioni del programma     
    '''

    def __init__(self,Main):
       
        super(Option, self).__init__()
        self.ui = OPTION_GUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.MainPadre = Main
        self.__IP_list =[]
        self.__timer = self.MainPadre.freq
        self.config = configparser.ConfigParser()
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        #self.__timer
    
    def set_Opt_Timer(self,timer):
        '''
        Setta il timer di aggiornamento preso dal valore della SpinBox
        '''
        self.__timer = timer
        self.ui.doubleSpinBox.setValue(timer)
        self.MainPadre.set_Timer(self.__timer)
    
    def accept (self):
        
        '''
        Tasto Ok dell'interfaccia
        Salva nel programma il valore del timer selezionato
        ''' 
        #Modifico il __timer
        spin_timer =self.ui.doubleSpinBox.value()
        self.set_Opt_Timer(spin_timer)
        self.hide()
    

    def load_settings (self,file = None):
        '''
        Caricamento Impostazioni, legge da file il timer e gli host salvati
        '''
        self.__timer =0
        self.__IP_list = []
        fName = file
        
        #vuotiamo la lista prima di riempirla
        
        
        if (not(fName)):
            fName = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.',filter ="*.cfg")
            
        print("Load ",fName)
        try:
            self.MainPadre.Clear_list()
            #READ
            self.config.read(fName)
            cfg_timer= float(self.config["Timer"]["Timer"])
            
            
            #settiamo il __timer
            self.set_Opt_Timer(cfg_timer)
            
            N_HOST = int(self.config["IP_LIST"]["num_host"])
            if (N_HOST !=0):
                print("NO ZERO HOST")
                self.__IP_list=(self.config["IP_LIST"]["IP"])
            #PRINT
            
            print("TIMER = ",self.__timer)
            print("N HOST",N_HOST)
            
            
            
            print("Lista IP",self.__IP_list)
            #vediamo se son presenti più di un host
            if (N_HOST != 0):
                if (str.find(self.__IP_list,",") != -1):
                    self.__IP_list=self.__IP_list.split(',')
                    N_HOST = len(self.__IP_list)
                
                    for i in range (N_HOST):
                        print("I = ",i)
                        IP = self.__IP_list[i]
                        print(IP)
                        j = IP.find("'")
                        k = IP.rfind("'")
                        print("Indici j{} k{} ".format(j,k))
                        print(IP[j+1:k])
                        self.MainPadre.crea_conn(IP[j+1:k])
                else:
                    IP = self.__IP_list
                    l = len(IP)
                    print(IP[2:l-2])
                    self.MainPadre.crea_conn(IP[2:l-2])
            
         
        except KeyError:
            self.MainPadre.dialogbox.showMessage("File di configurazione Corrotto o Errato")
    
    '''
    Salva su File .cfg il timer in uso e gli IP dei server monitorati
    '''
    
    def save_settings (self):
        
        self.config['Timer'] = {'Timer': str(self.__timer)}
        self.__IP_list = []
        
        for i in range (len(self.MainPadre.ui.host_w)):
            
            IP =self.MainPadre.ui.host_w[i].IP
            if IP != "LOCAL":
                self.__IP_list.append(IP)
                
        self.config['IP_LIST'] = { "NUM_HOST":len(self.MainPadre.ui.host_w)-1 ,"IP": self.__IP_list}
        
        fName = QtGui.QFileDialog.getSaveFileName(directory='.', filter='*.cfg')
        if (str.find(fName,".cfg")== -1):
            print("manca il cfg")
            fName+=".cfg"
        print(fName)
        F = open (fName,"w")
        self.config.write(F)
        F.close()
        print("Save of {} Done Correctly".format(fName))
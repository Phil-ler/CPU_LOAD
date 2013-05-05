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
        '''
        Constructor
        '''
        super(Option, self).__init__()
        self.ui = OPTION_GUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.MainPadre = Main
        self.IP_list =[]
        self.timer = self.MainPadre.freq
        self.config = configparser.ConfigParser()
        
        #self.timer
        
    def set_Timer(self):
        
        self.MainPadre.set_Timer(self.timer)
        
    def accept (self):
        #Modifico il timer
        self.timer =self.ui.doubleSpinBox.value()
        self.set_Timer()
        self.hide()
    def load_settings (self):
        self.timer =0
        self.IP_list = []
        fName = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.',filter ="*.cfg")
        print("Load ",fName)
        
        #RICORDARSI DI CHIAMARE LE FUNZIONI DI RIEMPIMENTO!!!
        try:
            #READ
            self.config.read(fName)
            self.timer= float(self.config["Timer"]["Timer"])
            
            N_HOST = int(self.config["IP_LIST"]["num_host"])
            if (N_HOST !=0):
                print("NO ZERO HOST")
                self.IP_list=(self.config["IP_LIST"]["IP"])
            #PRINT
            
            print("TIMER = ",self.timer)
            print("N HOST",N_HOST)
            
            
            #settiamo il timer
            self.set_Timer()
            
            
            
            print("Lista IP",self.IP_list)
            #vediamo se son presenti più di un host
            if (N_HOST != 0):
                if (str.find(self.IP_list,",") != -1):
                    self.IP_list=self.IP_list.split(',')
                    N_HOST = len(self.IP_list)
                
                    for i in range (N_HOST):
                        print("I = ",i)
                        IP = self.IP_list[i]
                        print(IP)
                        j = IP.find("'")
                        k = IP.rfind("'")
                        print("Indici j{} k{} ".format(j,k))
                        print(IP[j+1:k])
                        self.MainPadre.crea_conn(IP[j+1:k])
                else:
                    IP = self.IP_list
                    l = len(IP)
                    print(IP[2:l-2])
                    self.MainPadre.crea_conn(IP[2:l-2])
            
         
        except KeyError:
            self.MainPadre.dialogbox.showMessage("File di configurazione Corrotto o Errato")
    
    
    def save_settings (self):
        
        self.config['Timer'] = {'Timer': str(self.timer)}
        self.IP_list = []
        
        for i in range (len(self.MainPadre.ui.host_w)):
            
            IP =self.MainPadre.ui.host_w[i].IP
            if IP != "LOCAL":
                self.IP_list.append(IP)
                
        self.config['IP_LIST'] = { "NUM_HOST":len(self.MainPadre.ui.host_w)-1 ,"IP": self.IP_list}
        
        fName = QtGui.QFileDialog.getSaveFileName(directory='.', filter='*.cfg')
        if (str.find(fName,".cfg")== -1):
            print("manca il cfg")
            fName+=".cfg"
        print(fName)
        F = open (fName,"w")
        self.config.write(F)
        F.close()
        
        
        print("Save")
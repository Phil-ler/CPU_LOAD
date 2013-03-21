'''
Created on 20/mar/2013

@author: phil
'''
import psutil
from Host import Host

def main():
    print("CIAO")
    
    num_Host = psutil.NUM_CPUS
    My_Host = Host(num_Host)
    My_Host.Run(1)
 
 
    
if __name__ == '__main__':
    main()
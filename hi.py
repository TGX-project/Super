import socket 
from lib import config
def find_service_name(): 
    protocolname = 'http' 
    print ("Port: %s => service name: %s" %(port, socket.getservbyport(config.PORT, protocolname))) 
     
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))) 
     
if __name__ == '__main__': 
    find_service_name()

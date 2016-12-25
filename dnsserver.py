import socket, sys, constructDNS, responsePacket
from mapping import mapping

# Get the Source IP from the address which is input
def getSourceIP():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.connect(("google.com",80))
    return soc.getsockname()[0]

#Receive data from clients   
def receiveData():
    while True:
        global content, Clint_IP, port_Client, Nam, Ident
        sth = Reciev_Sock.recvfrom(65565)
        content=sth[0].strip()
        IP_ADD=sth[1]
        Clint_IP = IP_ADD[0]
        port_Client = IP_ADD[1]
        if content :
            Nam,Ident = constructDNS.MSG_DCODE_DNS(content)
            break

#Check the validation of the input
if (len(sys.argv) == 5):  
    Prt_Host = int(sys.argv[2])
    DMN_C = sys.argv[4]
else:
    print 'Please write the right arguments!'
    sys.exit()
host_ip = getSourceIP()   
#Listen packets from clients
while True:                     
    Reciev_Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            
    Reciev_Sock.bind((host_ip ,Prt_Host))
    receiveData()
    m=mapping()
    REP_IP_FIN=m.returnIP(Clint_IP)
    if (Nam == DMN_C):
        RES_DNS_PCKT = responsePacket.PCKT_RES(Nam,REP_IP_FIN,Ident)
        print 'Response the packet successfully!'
        soc = Reciev_Sock.sendto(bytes(RES_DNS_PCKT), 0, (Clint_IP,port_Client))
    else:
        print 'Receive the wrong domain'
        exit()
    Reciev_Sock.close()
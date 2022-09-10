import socket
import time
import pandas as pd
from datetime import datetime
import pytz
import random

#####Ping function by ip and port#####
retry = 1
delay = 1
timeout = 2

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def checkHost(ip, port):
    ipup = False
    for i in range(retry):
        if isOpen(ip, port):
            ipup = True
            break
        else:
            time.sleep(delay)
    return ipup

#####Check actual status of all IP-Port#####

# open the ip_port_list.txt file containing the list of ip addresses
    
print("Test actual status")
with open('ip_port_list.txt') as file:  
    dump = file.read()
    dump = dump.splitlines()
    
df = pd.DataFrame(columns=['HOST','IP','PORT','STATUS','DATE','PING_BEGINS','PING_ENDS'])
appendix = ""

    
for x in range(1,2):
    time.sleep(1)
    # Ping each ip-port adderess in the list    
    for i in dump:
        now = datetime.now(pytz.timezone('America/Bogota') ) 
        port = i.split()[2]
        ip = i.split()[1]
        host = i.split()[0]
        print('Start pinging:', ip, ':', port)
        if checkHost(ip, port):
            now2 = datetime.now(pytz.timezone('America/Bogota') )
            row = {'HOST':str(host), 'IP':str(ip),'PORT':str(port),'STATUS':'up', 'DATE':str(now.date()), 'PING_BEGINS':str('{: %H:%M:%S.%f}'.format(now)[:-3]), 'PING_ENDS':str('{: %H:%M:%S.%f}'.format(now2)[:-3])}
            df  = df.append(row, ignore_index=True)       
        else:
            now2 = datetime.now(pytz.timezone('America/Bogota') )
            row = {'HOST':str(host), 'IP':str(ip),'PORT':str(port),'STATUS':'down', 'DATE':str(now.date()), 'PING_BEGINS':str('{: %H:%M:%S.%f}'.format(now)[:-3]), 'PING_ENDS':str('{: %H:%M:%S.%f}'.format(now2)[:-3])}
            df  = df.append(row, ignore_index=True)
    
            
    #Check if all the connections are up to change the name of the file
    if 'down' in df.STATUS.values:
        appendix = "_Ip-Port_DownConns"
        print('Not all connections are up in this checking')
    else:
        appendix = "_Ip-Port"
        print('All connections are up in this checking')


csv_buffer = "out.csv"
df.to_csv(csv_buffer, index=False)

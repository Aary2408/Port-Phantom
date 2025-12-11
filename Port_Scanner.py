import socket
import sys
import time
import threading

usage = "python3 port_scaan.py TARGet start_port END_port"

print("_"*70)
print("")
print(''' ███████████     ███████    ███████████   ███████████     █████████    █████████    █████████   ██████   █████ ██████   █████ ██████████ ███████████  
░░███░░░░░███  ███░░░░░███ ░░███░░░░░███ ░█░░░███░░░█    ███░░░░░███  ███░░░░░███  ███░░░░░███ ░░██████ ░░███ ░░██████ ░░███ ░░███░░░░░█░░███░░░░░███ 
 ░███    ░███ ███     ░░███ ░███    ░███ ░   ░███  ░    ░███    ░░░  ███     ░░░  ░███    ░███  ░███░███ ░███  ░███░███ ░███  ░███  █ ░  ░███    ░███ 
 ░██████████ ░███      ░███ ░██████████      ░███       ░░█████████ ░███          ░███████████  ░███░░███░███  ░███░░███░███  ░██████    ░██████████  
 ░███░░░░░░  ░███      ░███ ░███░░░░░███     ░███        ░░░░░░░░███░███          ░███░░░░░███  ░███ ░░██████  ░███ ░░██████  ░███░░█    ░███░░░░░███ 
 ░███        ░░███     ███  ░███    ░███     ░███        ███    ░███░░███     ███ ░███    ░███  ░███  ░░█████  ░███  ░░█████  ░███ ░   █ ░███    ░███ 
 █████        ░░░███████░   █████   █████    █████      ░░█████████  ░░█████████  █████   █████ █████  ░░█████ █████  ░░█████ ██████████ █████   █████
░░░░░           ░░░░░░░    ░░░░░   ░░░░░    ░░░░░        ░░░░░░░░░    ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ 
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      ''')
print("Port Scanner")
print("           *****   CREATED BY AARY GAIKWAD   *****")
print("_"*70)

if(len(sys.argv)!=4):
    print(usage)
    sys.exit

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("scanning target",target)

def scan_port(port):
    print("Scanning port:",port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(10)
    conn = s.connect((target,port))
    if(not conn):
        print("Port {} is  Open".format(port))
    s.close()

for port in range (start_port,end_port+1):

    thread = threading.Thread(target = scan_port,args = (port,))
    thread.start() 


print("PRESS CTRL+C TO EXIT")

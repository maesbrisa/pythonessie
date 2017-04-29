#! /bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 3:
    print("python stealth_scan.py <ip> <ports>")
    exit()
src_port = RandShort()
dst_ip = sys.argv[1]
ports = sys.argv[2]

ports.replace(" ", "")
scanPorts = ports.strip().split(':')
for port in scanPorts:
    response = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=int(port),flags="S"))
    if(str(type(response))=="<type 'NoneType'>"):
        print(port+" Port Filtered")
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
         send_rst=sr1(IP(fst=dst_ip)/TCP(sport=src_port,dport=int(port),flags="R"))
         print(port+" Port Open")
    elif(response.getlayer(TCP).flags == 0x14):
         print(port+" Port Closed")
    elif(response.haslayer(ICMP)):
        if(int(response.getLayer(ICMP).type)==3 and
                int(response.getLayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print (port+": Filtered")

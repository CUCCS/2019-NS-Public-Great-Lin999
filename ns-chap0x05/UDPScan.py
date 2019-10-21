from scapy.all import *

dst_ip = "172.16.111.134"
src_port = RandShort()
dst_port=68

udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=10)
#print(udp_scan_resp.show())
if (str(type(udp_scan_resp))=="<type 'NoneType'>"):
    print(str(dst_port)+" is open|filter")
elif (udp_scan_resp.haslayer(UDP)):
    print(str(dst_port)+" is open")
elif(udp_scan_resp.haslayer(ICMP)):
    if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
        print(str(dst_port)+" is close")
    elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
        print(str(dst_port)+" is filter")
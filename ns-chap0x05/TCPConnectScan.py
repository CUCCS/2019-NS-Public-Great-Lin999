from scapy.all import *

dst_ip = "172.16.111.134"
src_ip = "172.16.111.120"
scr_port=RandShort()
dst_port=111


TCPConnectScanResponse = sr1(IP(src=src_ip,dst=dst_ip)/TCP(sport=scr_port,dport=dst_port),timeout=10)

if(str(type(TCPConnectScanResponse))=="<type 'NoneType'>"):
    print(str(dst_port)+" is Filter")
elif(TCPConnectScanResponse.haslayer(TCP)):
    if(TCPConnectScanResponse.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=scr_port,dport=dst_port,flags="AR"),timeout=10)
        print(str(dst_port)+" is open")
    elif(TCPConnectScanResponse.getlayer(TCP).flags == 0x14):
        print(str(dst_port)+" is close")
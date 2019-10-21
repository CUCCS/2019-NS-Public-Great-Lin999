from scapy.all import *

dst_ip = "172.16.111.134"
src_port = RandShort()
dst_port=111

null_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags=""),timeout=10)
if (str(type(null_scan_resp))=="<type 'NoneType'>"):
    print(str(dst_port)+" is Open|Filtered")
elif(null_scan_resp.haslayer(TCP)):
    if(null_scan_resp.getlayer(TCP).flags == 0x14):
        print(str(dst_port)+" is Closed")
#elif(null_scan_resp.haslayer(ICMP)):
#    if(int(null_scan_resp.getlayer(ICMP).type)==3 and int(null_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
#        print(str(dst_port)+" is Filtered")
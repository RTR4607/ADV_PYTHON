import socket
import re
l=['192.168.149.128','192.168.122.1','10.10','4000.233.1.1','100.100.100.100.']
ip=[]
ip1=[]
for s in l:
    b=re.findall(r'\.',s)
    if len(b)==3:
        ip.append(s)
print(ip)
for i in ip:
    try:
        socket.inet_aton(i)
        ip1.append(i)
    except Exception as ex:
        print(ex)
print(ip1)
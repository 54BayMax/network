#coding:utf-8
import socket

#ip:127.0.0.1,port 3214
HOST=''
PORT=3214

#AF_INET IPV4
#SOCK_DGRAM UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))

data=True
while data:
    data,addr=s.recvfrom(1024)
    if data == b'bye':
        break
    print 'Receive String:',data.decode('utf-8')
    s.sendto(data,addr)
s.close()
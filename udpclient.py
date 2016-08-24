#coding:utf-8
import socket

HOST='127.0.0.1'
PORT=3214

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data='Hello UDP server!'

while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data == 'bye':
        break
    recv_data,addr=s.recvfrom(1024)
    print 'Receive from Server:\n',recv_data.decode('utf-8')
    data=raw_input('Please input an info:\n')
s.close()

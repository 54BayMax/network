#coding:utf-8
import socket

#Host=''表示为本机地址
HOST=''
PORT=3214

#默认为IPV4,TCP协议
s=socket.socket()
s.bind((HOST,PORT))

s.listen(5)

clnt,addr=s.accept()

print "TCP Client Address:",addr

while True:
    data=clnt.recv(1024)
    if not data:
        break
    #把二进制解码为utf-8
    print 'receive data:',data.decode('utf-8')
    clnt.send(data)
clnt.close()
s.close()
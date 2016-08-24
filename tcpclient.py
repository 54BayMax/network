import socket

#ip:127.0.0.1,port 3214
HOST='' #warning:Ip addr can only be dropped in server!
PORT=3214

#AF_INET IPV4
#SOCK_DGRAM UDP
s=socket.socket()

#try to receive data from server & send data to server
#Pay attention to try statement .Client need connect to server in tcp,so you may catch exceptions,
#while in udp you just receive and send data!
try:
    s.connect((HOST,PORT))
    data=u'Hello TCP Server!'
    while data:
        #encode data from utf-8  to bytes
        s.sendall(data.encode('utf-8'))
        recv_data=s.recv(1024)
        #decode data from bytes to utf-8
        print 'Receive from Server:\n',recv_data.decode('utf-8')
        data=raw_input('Please input an info:\n')
except socket.error as err:
    print err
finally:
    s.close()

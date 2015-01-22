# Echo client program
import socket
import time

HOST = '192.168.1.102'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('1.wav')
#data = s.recv(1024)
#print 'Received', repr(data)
time.sleep(2)
s.send('2a.wav')
#data = s.recv(1024)
#print 'Received', repr(data)
time.sleep(2)
s.send('close')
#data = s.recv(1024)
#print 'Received', repr(data)
s.close()

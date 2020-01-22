import socket

try:
	s=socket.socket()
except socket.error as e:
	print("unsucessful :%s"%e)
	system.exit(0)
port=5555
s.connect(('127.0.1.1',port))
s.settimeout(5)
try:
	print s.recv(1024)
except socket.timeout as e:
	print("timeout!!!!!")
s.close()
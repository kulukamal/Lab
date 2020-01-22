import socket
import datetime
import time
try:
	s=socket.socket()
except socket.error as e:
	print("unsucessful :%s"%e)
	system.exit(0)

print("socket created successfully")
port=5555

try:
	s.bind(('',port))
	print("socket binded to port %s",port)
except Exception as e:
	print("port already in use.")
	system.exit(0)

s.listen(5)
print("socket is listening")

while(1):
	now = datetime.datetime.now()
	k=str(now)
	c,addr=s.accept()
	print("got connection from %s",addr)
	time.sleep(1)
	c.send(k)
	c.close()
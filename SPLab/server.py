# import socket
# import datetime
# s=socket.socket()
# print("socket created successfully")

# port=5555

# s.bind(('',port))
# print("socket binded to port %s",port)

# s.listen(5)

# print("socket is listening")



# while(1):
# 	now = datetime.datetime.now()
# 	k=str(now)
# 	c,addr=s.accept()
# 	print("got connection from %s",addr)
# 	c.send(k)
# 	c.close()

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234 if len(sys.argv) == 1 else int(sys.argv[1])
sock.bind(('localhost', port))
sock.listen(5)

try:
    while True:
        conn, info = sock.accept()

        data = conn.recv(1024)
        while data:
            print data
            data = conn.recv(1024)
except KeyboardInterrupt:
    sock.close

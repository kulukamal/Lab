import socket 
 
outSize = 0
inSize = 0

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 

outSizeBefore = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
inSizeBefore = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print(outSizeBefore,inSizeBefore)

s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, outSize)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, inSize)

outSizeBefore = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
inSizeBefore = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print(outSizeBefore,inSizeBefore)

# port = 1234
# s.bind(('localhost', port))
# s.listen(5)

# try:
#     while True:
#         conn, info = s.accept()
#         data = conn.recv(inSize)
#         print data
# except KeyboardInterrupt:
#     s.close
# import socket

# s=socket.socket()
# port=5555
# s.connect(('127.0.1.1',port))
# s.settimeout(5)
# print s.recv(1024)
# s.close()


# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('localhost', 1234))
# sock.setblocking(0)
# data = 'foobar\n' * 10 * 1024 * 100  # 70 MB of data
# assert sock.send(data) == len(data)  # True
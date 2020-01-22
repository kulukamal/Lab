import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1234))
sock.setblocking(1)
data = 'foobar\n' * 10 * 1024 * 100  # 70 MB of data
assert sock.send(data) == len(data)  # True
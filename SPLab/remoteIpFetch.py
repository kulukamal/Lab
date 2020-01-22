import socket
from binascii import hexlify
def map(dec):
	if dec < 10:
		return dec
	elif dec == 10:
		return 'a'
	elif dec == 11:
		return 'b'
	elif dec == 12:
		return 'c'
	elif dec == 13:
		return 'd'
	elif dec == 14:
		return 'e'
	else:
		return 'f'
def Hex(dec):
	h = ''
	h = str(map(dec % 16))
	dec = dec / 16
	h = str(map(dec % 16)) + h
	return h
def Bin(dec):
	b = ''
	for i in range(8):
		b = str(dec % 2) + b
		dec = dec / 2
	return b

def Oct(dec):
	o = ''
	for i in range(3):
		o = str(dec % 8) + o
		dec = dec / 8
	return o

host = 'pool.ntp.org'
try:
	ip = socket.gethostbyname(host)
	print("IP address: " + ip)
	lip = ip.split('.')
	hexIp = ''
	binIp = ''
	octIp = ''
	for l in lip:
		hexIp = hexIp + '.' +Hex(int(l))
		binIp = binIp + '.' +Bin(int(l))
		octIp = octIp + '.' +Oct(int(l))
	print(hexIp[1:])
	print(binIp[1:])
	print(octIp[1:])
	

except socket.error, err:
	print(host, err)
import socket
from urlparse import urlparse
protocols = [ 'tcp', 'udp']

for protocol in protocols:
	for port in range(100):
		try :
			print("port : " , port , " service name : " , socket.getservbyport(port, protocol) , " protocol : ",protocol)
		except socket.error, err:
			pass

# hosts = [ 'http://www.python.org',
#              'https://www.mybank.com',
#              'ftp://prep.ai.mit.edu',
#              'gopher://gopher.micro.umn.edu',
#              'smtp://mail.example.com',
#              'imap://mail.example.com',
#              'imaps://mail.example.com',
#              'pop3://pop.example.com',
#              'pop3s://pop.example.com',
#         ]

# port = 80


# for host in hosts:
# 	scheme = urlparse(host).scheme
# 	try :
# 		print(scheme, socket.getservbyname(scheme))
# 	except socket.error, err:
# 		print(err)
import socket
def get_host_name():
	return socket.gethostname()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("15.24.11.24", 80))
    return s.getsockname()[0]

print(get_host_name())
print(get_ip_address())
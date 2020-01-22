import socket 
import sys 


local_port = 8282 
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
srv.bind( ('', local_port) ) 
srv.listen(1) 
print ("Listening on port: %s " %local_port) 
while True: 
    try: 
        connection, addr = srv.accept() 
        print ('Connected by %s:%s'
                % (addr[0], addr[1])) 
    except KeyboardInterrupt: 
        break 
    except socket.error as msg: 
        print ('%s' % (msg,)) 
 
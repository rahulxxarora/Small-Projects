# TCP uploading client
import socket
import getpass
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
mode = "2"
client_socket.send(mode)
f = open('/home/rahul/CLOUD/data.txt','r')

print "Connected"
while 1:
   data = f.readline()  
   if not data:
      client_socket.close()
      f.close()
      break
   else:
      client_socket.send(data)
   
print "DONE"

            

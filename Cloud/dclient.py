# TCP downloading client 
import socket
import getpass
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
mode = "1"
client_socket.send(mode)
f = open('/home/rahul/CLOUD/data.txt','w')

print "Connected"
while 1:
   data = client_socket.recv(512)
   if not data:
      client_socket.close()
      f.close()
      break
   f.write(data.strip())

print "DONE"
   

            

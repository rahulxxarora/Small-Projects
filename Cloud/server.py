# TCP server
import socket
import time
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen(1)

print "TCPServer Running"

while 1:
   client_socket, address = server_socket.accept()
   print "Request from ", address
   data = client_socket.recv(512)
   if data=='1':
      f = open('/home/rahul/CLOUD/DATA_CLOUD/data.txt','r')
      print "Uploading to ", address
      time.sleep(0.5)
      while 1:
         data = f.readline()  
         if not data:
            client_socket.close()
            f.close()
            break
         else:
            client_socket.send(data)
   else:
      f = open('/home/rahul/CLOUD/DATA_CLOUD/data.txt','w')
      print "Downloading from ", address
      time.sleep(0.5)
      while 1:
         data = client_socket.recv(512)
         if not data:
            client_socket.close()
            f.close()
            break
         f.write(data.strip())
   
        

      	
 

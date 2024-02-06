import socket

host = 'localhost'
port = 1234

#creating a point of connection for connection 
s= socket.socket()

#binding 
s.bind((host,port))

#maximum connection 
s.listen(1)

#waiting for client cconnection 
c, addr = s.accept()

#client connection conformation
print("Client Connected")
print("connection from : ",str(addr))

while 1:
    #receive 
    data = c.recv(1024)

    if not data:
        break
    print("from client :",str(data.decode()))

    data1 = input("server: ")

    c.send(data1.encode())

c.close()





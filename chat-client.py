import socket

host = '127.0.0.1'
port = 1234

#creating a point of connection for connection 
s= socket.socket()

#server connection 
s.connect((host, port))

str = input("cLIENT : ")

while str!= 'exit':
    #send
    s.send(str.encode())

    #receive
    data= s.recv(4000)
    data = data.decode()
    print("From server : ",data)

    #send 
    str= input("cLIENT: ")

#connection closing 
s.close()


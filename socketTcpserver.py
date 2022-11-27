
import socket

#creating socket object and specifying the socket family and type of connection which is TCP connection oriented 

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sockets are outlet that allows you to send and  receive internal endpoint connection
#gethostbyname will collect all the ip  address of the client machine and display them

host=socket.gethostbyname()
#specify the port the host will listen to
port=444
#we have to bind  the server socket family to host and port that it is listening to
serversocket.bind((host,port))
#we have to listen to the connection that we created
serversocket.listen(3)
while True:
    #creating the client socket to accept the tcp information from the server
    clientsocket,address=serversocket.accept()
    print('received connecton from' %str(address))
    message='thankyou for connecting with us'+ '\r\n'
    clientsocket.send(message)
    clientsocket.close































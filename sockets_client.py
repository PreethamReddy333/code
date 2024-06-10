import socket
myserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myserver.connect((socket.gethostname(), 1024))
# 1024 is same port number given in server
msg=myserver.recv(1024)
# 1024 bytes is is just sample byte number. Received
#message from Server is stored in “msg”
print(msg.decode("utf-8"))
# "utf-8" is bytes code given in server. Message received
#from the Server can be decoded.



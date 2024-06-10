import socket
myserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET referes the address from the Internet and
#SOCK_STREAM is used to create TCP protocol
myserver.bind((socket.gethostname(), 1024))
#Here 1024 is the Port Number.
#Provide any Port number is>1023 which is non previliged.
myserver.listen(5)
#This asks for permission on Windows
while True:
    myclient,addr=myserver.accept()
    print(f"Connection to {addr} established")
    # f string is literal string
    myclient.send(bytes("Welcome to Socket Programming in  Python!", "utf-8"))
    # To pass the message from server to client.
    #The kind of byte is utf-8 (Unicode Transformation Format – 8-bit)

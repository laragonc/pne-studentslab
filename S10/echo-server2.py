import socket
import termcolor
# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.140" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

count = 1
flag = True
while flag:
    (rs, address) = ls.accept()# returns total socket and the adress
    msg = rs.recv(2048).decode("utf-8") #readed from client and tranform to utf
    print("CONECTION", count, "Client IP, PORT: ", address)
    print("Message received: " + termcolor.colored(msg, "green"))
    rs.send(msg.encode()) #encode to bites and then send it
    count += 1
    rs.close()
ls.close()
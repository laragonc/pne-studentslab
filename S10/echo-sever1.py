import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.140" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
while True:
    (rs, address) = ls.accept()# returns total socket and the adress
    print(f"Client {address}")
    msg = rs.recv(2048).decode("utf-8") #readed from client and tranform to utf
    print("Message received: " + termcolor.colored(msg, "green"))
    newMsg = "ECHO: " + msg
    rs.send(newMsg.encode()) #encode to bites and then send it
    rs.close()
ls.close()
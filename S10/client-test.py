from Client0 import *
import termcolor
IP = "212.128.255.140"
PORT = 8080
c = Client(IP, PORT)
count = 0
while count < 5:
    message = input("Enter a message:")
    count += 1
    print("To server:" + termcolor.colored(message, "blue"))
    response = c.talk(message)
    print("From server:", termcolor.colored(response, "green"))


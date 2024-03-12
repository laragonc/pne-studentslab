from Client0 import *
import termcolor
PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
flag = True
while flag:
    message = input("Enter a number from 0-100:")
    print("To server:" + termcolor.colored(message, "blue"))
    response = c.talk(message)
    if response.startswith("You guessed it!"):
        print("From server:", termcolor.colored(response, "green"))
        flag = False
    else:
        print("From server:", termcolor.colored(response, "green"))

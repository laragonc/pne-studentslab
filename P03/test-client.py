from Client0 import *
import termcolor
PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
message = "PING"
print("* Testing " + message + "...")
response = c.talk(message)
print(response)

message = "GET 1"
print("* Testing " + message + "...")
response = c.talk(message)
print(response)

message = "INFO AAACTGG"
print("* Testing " + message + "...")
response = c.talk(message)
print(response)

message = "COMP AAACTGG"
print("* Testing " + message + "...")
response = c.talk(message)
print(response)

message = "GENE U5"
print("* Testing " + message + "...")
response = c.talk(message)
print(response)



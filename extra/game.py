import socket
import random
class NumberGuesser:
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"
        MAX_OPEN_REQUESTS = 5
        number_con = 0
        self.secret_number = random.randint(1, 100)
        self.attempts = []

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen(MAX_OPEN_REQUESTS)

            while True:
                # accept connections from outside
                print("Waiting for connections at {}, {} ".format(IP, PORT))
                (clientsocket, address) = serversocket.accept()

                # Another connection!e
                number_con += 1

                # Print the connection number
                print("CONNECTION: {}. From the IP: {}".format(number_con, address))

                # Read the message from the client, if any
                number = clientsocket.recv(2048).decode("utf-8")#LO QUE RECI
                print("Message from client: {}".format(number))

                # Send the message
                message = self.guess(number)
                send_bytes = str.encode(message)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()
    def guess(self, number):
        if self.secret_number > int(number):
            value = "Higher! "
            self.attempts.append(number)
        elif self.secret_number < int(number):
            value = "Lower! "
            self.attempts.append(number)
        else:
            value = "You guessed it!, the number is: " + str(self.secret_number) + " Number of attempts: " + str(len(self.attempts))
        return value

c = NumberGuesser()

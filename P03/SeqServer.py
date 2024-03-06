import socket
class SeqServer():
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"  # it depends on the machine the server is running
        MAX_OPEN_REQUESTS = 5

        # Counting the number of connections
        number_con = 0

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
                msg = clientsocket.recv(2048).decode("utf-8")#LO QUE RECI
                print("Message from client: {}".format(msg))

                # Send the message
                message = self.return_response(str(msg))
                send_bytes = str.encode(message)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    def return_response(self, msg):
        if msg.startswith("PING"):
            print("PING")
            return self.ping_response()
        if msg.startswith("GET"):
            print("GET")
            return self.get_response(msg)
    def ping_response(self):
        print("PING command")
        return "ok\n"
    def get_response(self, msg):
        number = 0
        list_sequences = ["ACTGGACTGGTTCA", "CTGGAATCGTACG", "TACGTACTGAACGT", "GTAGCTACTGCTAGT", "ACTTGGAAGGTCAC"]
        for i in msg:
            if i.isdigit():
                number = i
            else:
                pass
        return list_sequences[int(number)]
hg
c = SeqServer()
from Client0 import Client
from Seq1 import *
genes = ["U5", "ADA", "FRAT1"]
genes_dir = "../sequences/"

PRACTICE = 2
EXERCISE = 4

def get_file_path(gene):
    return genes_dir + gene
def req_response_from_server(client, msg):
    print("To Sever: {}".format(msg), sep="")
    response = client.talk(msg)
    print(f"From Server:{response}")
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.64"
PORT = 8081

c = Client(IP, PORT)
for g in genes:
    s = Seq()
    s.read_fasta(get_file_path(g))
    m = "Sending " + g + " Gene to the server..."
    req_response_from_server(c, m)
    m = str(s)
    req_response_from_server(c, m)
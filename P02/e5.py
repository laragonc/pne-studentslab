from Client0 import Client
from Seq1 import *
genes = ["U5", "ADA", "FRAT1"]
genes_dir = "../sequences/"

PRACTICE = 2
EXERCISE = 5

IP = "172.20.10.3"
PORT = 8081
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
def get_file_path(gene):
    return genes_dir + gene
def req_response_from_server(client, msg):
    print("To Sever: {}".format(msg), sep="")
    response = client.talk(msg)
    print(f"From Server:{response}")
def create_fragment(sequence):
    fragment = ""
    count = 0
    fragment_list = []
    for i in sequence:
        count += 1
        fragment += 1
        if count == 10:
            fragment_list.append(fragment)
            fragment = ""
            count = 0
    if fragment:
        fragment_list.append(fragment)
    return fragment_list
c = Client(IP, PORT)
for g in genes:
    s = Seq()
    s.read_fasta(get_file_path(g))
    m = "Sending " + g + " Gene to the server..."
    req_response_from_server(c, m)
    m = str(s)
    req_response_from_server(c, m)
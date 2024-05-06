import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import *
# Define the Server's port
PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_response(number):
    list_sequences = ["ACTGGACTGGTTCA", "CTGGAATCGTACG", "TACGTACTGAACGT", "GTAGCTACTGCTAGT", "ACTTGGAAGGTCAC"]
    return list_sequences[int(number)]
def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    seq = Path(filename).read_text()[first_line:]
    seq = seq.replace("\n", "")
    return seq
def seq_reverse(seq):
    reverse = seq[::-1]
    return reverse
def seq_complement(seq):
    complement = ""
    for i in seq:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement


def info_response(seq):
    sequence = ""
    for i in seq:
        if i in "ACGT":
            sequence += i
    bases_list = ["A", "C", "T", "G"]
    result = f"Total length: {len(seq)}\n"
    for j in bases_list:
        average = (round(seq.count(j) / len(seq) * 100, 2))
        result += f"{j}: {seq.count(j)} ({average}%)\n"
    return result





# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if path == "/" or path.startswith("/echo"):
            contents = Path("./html/index.html").read_text()
            self.send_response(200)

        elif path == "/ping":
            contents = Path("./html/ping.html").read_text()
            self.send_response(200)
        elif path == "/get":
            number = arguments.get("n", [""])[0]
            sequence = get_response(number)
            contents = read_html_file("get.html").render(context={"number": number, "sequence": sequence})
            self.send_response(200)
        elif path == "/gene":
            gene_name = arguments.get("name", [""])[0]
            sequence = seq_read_fasta("../sequences/" + gene_name)
            contents = read_html_file("gene.html").render(context={"gene_name": gene_name, "sequence": sequence})
            self.send_response(200)
        elif path == "/operation":
            sequence = arguments.get("msg", [""])[0]
            operation = arguments.get("op", [""])[0]
            if operation == "info":
                result = info_response(sequence)
            elif operation == "rev":
                result = seq_reverse(sequence)
            elif operation == "comp":
                result = seq_complement(sequence)
            contents = read_html_file("operation.html").render(context={"sequence": sequence, "operation": operation, "result": result})
            self.send_response(200)

        else:
            contents = Path("./html/error.html").read_text()
            self.send_response(404)


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
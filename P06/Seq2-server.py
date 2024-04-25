import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

# Define the Server's port
PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    seq = Path(filename).read_text()[first_line:]
    seq = seq.replace("\n", "")
    return seq

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if self.path == "/" or self.path.startswith("/echo"):
            contents = Path("./html/index.html").read_text()
            self.send_response(200)
            url_path = urlparse(self.path)
            path = url_path.path # we get it from here
            arguments = parse_qs(url_path.query)
            ping = arguments.get("ping", [""])[0]
            if ping:
                contents = Path("./html/ping.html").read_text()
                self.send_response(200)
            else:
                contents = Path("./html/index.html").read_text()
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
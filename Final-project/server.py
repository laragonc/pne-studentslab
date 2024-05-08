import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import json
# Define the Server's port
PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_path(ENDPOINT):
    PARAMS = "?content-type=application/json"
    path = ENDPOINT + PARAMS
    return path


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

        if path == "/" or path.startswith("/echo"):
            contents = Path("./html/index.html").read_text()
            self.send_response(200)
        elif path == "/listSpecies":
            SERVER = "rest.ensembl.org"

            limit = int(arguments.get("limit", [""])[0])
            conn = http.client.HTTPConnection(SERVER)
            try:
                conn.request("GET", get_path("/info/species"))
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                info = json.loads(data)
                species = info["species"]

                for i in species:


            except ConnectionRefusedError:
                print("ERROR! Cannot conect to the server")
                exit()

        elif path == "/karyotype":
            pass
        elif path == "/chromosomeLength":
            pass
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
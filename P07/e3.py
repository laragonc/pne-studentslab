import http.client
import json
import termcolor
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print("Server:", SERVER)
print("URL:", URL)

conn = http.client.HTTPConnection(SERVER)
try:
    conn.request("GET", ENDPOINT + PARAMS)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    parsed_data = json.loads(data)

    # Extracting server name from the headers
    server_name = response.getheader("Server")

    print("Response received!: {} {}".format(response.status, response.reason))
    print("Gene: MIR633")
    print("Description:", parsed_data["desc"])
    print("Bases:", parsed_data["seq"])

except KeyboardInterrupt:
    print("")
    print("Stopped by the user")
    conn.close()



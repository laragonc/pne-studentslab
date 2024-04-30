import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
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
    print("PING OK! {}".format(parsed_data["ping"]))

except KeyboardInterrupt:
    print("")
    print("Stopped by the user")
    conn.close()

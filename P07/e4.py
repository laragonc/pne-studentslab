import http.client
import json
import termcolor
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
genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}
gene_name = input("Enter a gene name: ")
if gene_name in genes:
    code = genes[gene_name]
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/" + str(code)
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
    sequence = parsed_data["seq"]

    print("Response received!: {} {}".format(response.status, response.reason))
    print("Gene: " + str(gene_name))
    print("Description:", parsed_data["desc"])
    print(info_response(sequence))

except KeyboardInterrupt:
    print("")
    print("Stopped by the user")
    conn.close()
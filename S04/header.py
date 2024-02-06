from pathlib import Path
FILENAME = "sequences/RNU6_269P"
file_contents = Path(FILENAME).read_text()
file_header = file_contents.split("\n")
header = file_header[0]
print(header)


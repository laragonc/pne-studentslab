from pathlib import Path
FILENAME = "sequences/RNU6_269P"
file_contents = Path(FILENAME).read_text()
list_contents = file_contents.split("\n")
for i in range(1, len(list_contents)):
    print(list_contents[i])

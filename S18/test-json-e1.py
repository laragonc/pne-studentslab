import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
data = json.loads(jsonstring)

# Print the information on the console, in colors
print()
for person in data:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])
    termcolor.cprint("Phone numbers: ", 'green', end='')
    for i, number in enumerate(person['phoneNumber'], 1):
        termcolor.cprint("\n  Phone " + str(i) + ": ", 'blue')
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(number['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(number['number'])



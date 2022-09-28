import sys
import clipboard as copi
import json

# AUTHOR : AJBAR Imad #

"""
i recommend you to read REDME first, that will help you to more understant the multi-clipboard project.
"""

SAVED_FILE = "clipboard.json"

# save data in our clipboard (json file)
def save_data(filePath, data):
    with open(filePath, 'w') as f:
        json.dump(data, f)

# read from our json file
def load_data(filePath):
    try: # handle exception if the file not exist yet
        with open(filePath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

# accept one or two arguments
if len(sys.argv) == 2 or len(sys.argv) == 3:
    command = sys.argv[1]
    data = load_data(SAVED_FILE)

    if command == "save":
        key = input("Enter a key: ")
        value = input("Enter the data you want to store: ")
        data[key] = value
        save_data(SAVED_FILE, data)
        print("Data saved !")

    elif command == "load":
        key = sys.argv[2]
        if key in data:
            copi.copy(data[key])
            print("Data copied to clipboard !")
        else:
            print("Key does not exist !")

    elif command == "list":
        if len(data) == 0:
            print("clipboard.json is empty!")
        else:
            for key in data:
                print(key + ": " + data[key])

    else:
        print("Unknown command !")
else:
    print('''Save data: "python multiClipboard.py save"
\nLoad data to clipboard: "python multiClipboard.py load <key>"
\nList all the keys and values: "python multiClipboard.py list"''')

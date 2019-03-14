import json

filename = 'textFiles/username.json'

with open(filename, 'w') as fileObj:
    json.dump('varun', fileObj)
    fileObj.close()

with open(filename, 'r') as readFileObj:
    nameRead = json.load(readFileObj)
    print("Name read: " + nameRead)
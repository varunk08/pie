import json
print('Reads json file.')
prompt = 'Enter file name: '
filename = input(prompt)

with open(filename) as fileObj:
    text = json.load(fileObj)
    print(text)
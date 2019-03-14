filename = 'textFiles/sample1.txt'

with open(filename, 'w') as fileObject:
    for number in range(1,101):
        fileObject.write(str(number) + " Hello world of files. \n")
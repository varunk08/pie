import os
from os import path

filePath = str(input('Enter directory: '))

print(filePath)

if path.isabs(filePath):
	if path.exists(filePath):
		if path.isdir(filePath):
			contents = os.listdir(filePath)
			totalSize = 0
			for item in contents:
				print(item)
				totalSize += os.path.getsize(os.path.join(filePath, item))
			print("Total size: " + str(totalSize) + ' bytes')
		else:
			print('Pls enter a directory path')
	else:
		print("The folder doesn't exist")
else:
	print("Pls enter absolute path")
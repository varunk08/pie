import os

path = os.path.join('hello', 'world')
print(path)
print(os.path.join('hello','dear'))

myfiles = ['kiity', 'kat']

for filename in myfiles:
	print(os.path.join('C:\\user\\', filename))

print (os.getcwd())

#os.makedirs(os.path.join(os.getcwd(), 'test_dir'))


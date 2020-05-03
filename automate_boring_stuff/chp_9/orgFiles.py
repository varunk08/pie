#! python3
import shutil
import os
import send2trash
import zipfile

print('Simple script for expt with shutil')

os.chdir('testDirA')
testFile = open('testFile.txt', 'w')
testFile.write('This is a test text')
testFile.close()

shutil.copy('testFile.txt', r'..\testDirB\testFileB.txt')
testFileB = open('..\\testDirB\\testFileB.txt')
print('Written to file: ' + testFileB.read())
testFileB.close()

shutil.copytree('..\\testDirB', '..\\testDirC')

#shutil.move()
#os.unlink()
#os.rmtree()
#os.rmdir()
#os.listdir()
#string.endswith()

os.chdir('..\\')
print(os.listdir())

for folderName, subFolders, fileNames in os.walk(os.getcwd()):
    print(folderName)
    for subFolder in subFolders:
        print('Subfolder: ' + subFolder)
    for fileName in fileNames:
        print('File: ' + os.path.join(folderName, fileName))
    print('')

newZip = zipfile.ZipFile('compressed.zip', 'w')
if fileName != 'compressed.zip':
    newZip.write(os.path.join(fileName), compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

print('Deleting testDirC')
shutil.rmtree('testDirC')

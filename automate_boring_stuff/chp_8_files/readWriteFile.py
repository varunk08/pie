import os

poem = ''' And the Raven, never flitting, still is sitting, still is sitting
On the pallid bust of Pallas just above my chamber door;
    And his eyes have all the seeming of a demon’s that is dreaming,
    And the lamp-light o’er him streaming throws his shadow on the floor;
And my soul from out that shadow that lies floating on the floor
            Shall be lifted—nevermore!'''

filename = 'thePoem.txt'
myFile = open(filename, 'w')
myFile.write(poem)
myFile.close()

myFile = open(filename, 'r')
fromFile = myFile.read()
print(fromFile)
myFile.close()
from random import randint
import pygal


class Die():
    def __init__(self, numSides=6):
        self.numSides = numSides


    def roll(self):
        return randint(1, self.numSides)




#die = Die()
#
#results = []
#for rollNum in range(1000):
#    result = die.roll()
#    results.append(result)
#
#
#print(results)
#
#
#frequencies = []
#for value in range(1, die.numSides + 1):
#    frequency = results.count(value)
#    frequencies.append(frequency)
#
#print(frequencies)
#
#
#hist = pygal.Bar()
#hist.title = "resuls of rolling one D6 1000 times"
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
#hist.x_title = "Result"
#hist.y_title = "frequency of result"
#
#hist.add('D6', frequencies)
#hist.render_to_file('die_visual.svg')
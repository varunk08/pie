from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for rollNum in range(1000):
    result  = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
maxResult = die1.numSides + die2.numSides

for val in range(2, maxResult + 1):
    frequency = results.count(val)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Resuls of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 +  D6', frequencies)
hist.render_to_file('dice_visual2.svg')
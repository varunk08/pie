from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    def __init__(self, numpoints=50000):
        self.numPoints = numpoints
        self.x_values = [0]
        self.y_values = [0]


    def fillWalk(self):
        while len(self.x_values) < self.numPoints:
            xDir = choice([1, -1])
            xDist = choice([0, 1, 2, 3, 4])
            xStep = xDir * xDist

            yDir = choice([1, -1])
            yDist = choice([0, 1, 2, 3, 4])
            yStep = yDir * yDist

            if xStep == 0 and yStep == 0:
                continue

            nextX = self.x_values[-1] + xStep
            nextY = self.y_values[-1] + yStep

            self.x_values.append(nextX)
            self.y_values.append(nextY)


while True:
    rw = RandomWalk()
    rw.fillWalk()

    plt.figure(dpi=128, figsize=(10,6))
    pointNumbers = list(range(rw.numPoints))
    plt.scatter(rw.x_values, rw.y_values, c=pointNumbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keepRunning = input("Make another walk? (y/n):")
    if keepRunning == 'n':
        break
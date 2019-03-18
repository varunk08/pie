import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    highs=[]
    for row in reader:
        highs.append(row[1])

    print(highs)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(highs, c='red')
    plt.title('Daily high  temperatures, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
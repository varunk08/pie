import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dates, highs=[], []
    for row in reader:
        currentDate = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(currentDate)
        high = int(row[1])
        highs.append(high)

    print(highs)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    plt.title('Daily high  temperatures, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
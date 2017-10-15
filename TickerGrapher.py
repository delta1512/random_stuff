from matplotlib import pyplot
import csv

with open('/tmp/BTC', 'r') as BTCfile:
    read = csv.reader(BTCfile, dialect='unix')
    price = []
    time = []
    for ln in read:
        price.append(float(ln[0]))
        time.append(int(ln[1]))
    delta = max(time) - (max(time) - min(time))
    timeframe = max(time) - min(time)
    time = [i-delta for i in time]

pyplot.suptitle('Bitcoin price over ' + str(timeframe) + ' seconds')
pyplot.plot(time, price)
pyplot.show()

with open('/tmp/GRC', 'r') as GRCfile:
    read = csv.reader(GRCfile, dialect='unix')
    price = []
    time = []
    for ln in read:
        price.append(float(ln[0]))
        time.append(int(ln[2]))
    delta = max(time) - (max(time) - min(time))
    timeframe = max(time) - min(time)
    time = [i-delta for i in time]

pyplot.suptitle('Gridcoin price over ' + str(timeframe) + ' seconds')
pyplot.plot(time, price)
pyplot.show()

from urllib.request import urlopen
from random import randint
import json

rainy = [0, 1, 2, 3, 4, 6, 8, 9, 11, 12, 35, 38, 39, 40]
snowy = [5, 7, 10, 13, 14, 15, 16, 17, 18, 41, 42, 43, 46]
foggy = [19, 20, 21, 22]
lightning = [37, 38, 39, 45, 47]

try:
    JSON = json.loads(urlopen('example.com').read().decode())
    weather_code = int(JSON['index'])
except:
    weather_code = randint(0, 47)

output = 0

if weather_code in rainy:
    output = 1
elif weather_code in snowy:
    output = 2
elif weather_code in foggy:
    output = 3
elif weather_code in lightning:
    output = 4

with open('/tmp/weatherstate.txt', 'w') as weatherfile:
    weatherfile.write(str(output))

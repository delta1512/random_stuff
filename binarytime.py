from os import popen
from time import sleep
from sys import stdout

while True:
    print(str(bin(int(popen('date +%s').read())))[2:])
    sleep(1)

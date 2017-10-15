from urllib.request import urlopen
from time import sleep
import json

class BTCjson:
    price = None
    volume = None
    last_update = None

    def get(self):
        JSON = json.loads(urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin/').read().decode())[0]
        self.price = JSON["price_usd"]
        tmp = self.last_update
        self.last_update = int(JSON["last_updated"])
        if tmp == self.last_update:
            return None
        else:
            return self.price + ',' + str(self.last_update) + '\n'

class GRCjson:
    price_usd = None
    price_btc = None
    volume = None
    last_update = None

    def get(self):
        JSON = json.loads(urlopen('https://api.coinmarketcap.com/v1/ticker/gridcoin/').read().decode())[0]
        self.price_usd = JSON["price_usd"]
        self.price_btc = JSON["price_btc"]
        tmp = self.last_update
        self.last_update = int(JSON["last_updated"])
        if tmp == self.last_update:
            return None
        else:
            return self.price_usd + ',' + self.price_btc + ',' + str(self.last_update) + '\n'

BTC = BTCjson()
GRC = GRCjson()

while True:
    with open('/tmp/BTC', 'a') as BTCfile:
        data = BTC.get()
        while data == None:
            sleep(60)
            data = BTC.get()
        BTCfile.write(data)

    with open('/tmp/GRC', 'a') as GRCfile:
        data = GRC.get()
        while data == None:
            sleep(60)
            data = GRC.get()
        GRCfile.write(data)

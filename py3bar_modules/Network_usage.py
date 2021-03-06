# -*- coding: utf-8 -*-
import commands
class Py3status:
    def net(self):
        RX, TX = 0, 0
        interfaces = ['enp0s3'] #Choose interfaces here
        for x in interfaces:
            info = commands.getoutput('ifconfig ' + x + ' | grep RX | grep TX')
            found = False
            results = []
            for i, char in enumerate(info):
                if found or char == ':':
                    if char == ':':
                        results.append(i+1)
                    found = True
                    if char == ' ':
                        results.append(i)
                        found = False
            RX = RX + float(info[results[0]:results[1]])
            TX = TX + float(info[results[2]:results[3]])
        results = []
        for data in [RX, TX]:
            if 1000 < data < 1000**2:
                results.append(str(round(data / 1000, 2)) + 'kB')
            elif 1000**2 < data < 1000**3:
                results.append(str(round(data / 1000**2, 2)) + 'MB')
            elif 1000**3 < data < 1000**4:
                results.append(str(round(data / 1000**3, 2)) + 'GB')
            elif 1000**4 < data < 1000**5:
                results.append(str(round(data / 1000**4, 2)) + 'TB')
            else:
                results.append(str(data) + 'B')
        RX = results[0]
        TX = results[1]
        return {'full_text': '' + str(RX) + ' ' + '' + str(TX),
                'cached_until': self.py3.time_in(1)}

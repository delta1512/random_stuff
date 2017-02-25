#!/usr/bin/python3

import subprocess
from os import devnull
from sys import argv

try:
	arg = argv[1]
except:
	arg = None

FNULL = open(devnull, 'w')
proc = subprocess.call(['ping', '-c', '1', 'google.com'], stdout=FNULL, stderr=subprocess.STDOUT)
if proc == 0:
	if arg == '-s':
		print('connected')
	proc = subprocess.call(['ping', '-c', '1', 'proxy.det.nsw.edu.au'], stdout=FNULL, stderr=subprocess.STDOUT)
	if proc == 0:
		if arg == '-s':
			print('at school')
		else:
			proc = subprocess.Popen(['export', 'http_proxy=http://proxy.det.nsw.edu.au:8080/'])
			proc = subprocess.Popen(['export', 'https_proxy=http://proxy.det.nsw.edu.au:8080/'])
FNULL.close()

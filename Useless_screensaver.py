import os
import random
from time import sleep, clock
from sys import argv

if len(argv) == 1:
    argv.append(None)

global messages_j, messages_s, rows, cols
messages_j = ['Generating new random messages',
            'Reverting to a legacy kernel',
            'Moving all user data to /dev/null',
            'Sending SIGKILL to all processes',
            'Unfortunately time has stopped',
            'Currently signing in to string(USR_CLICK_EV(get_text()))',
            'Useless_screensaver.py has stopped responding',
            'Trying to find system32',
            'The entire internet crashed. Attempting to revive key infrastructure before it\'s too late',
            'Unmounting the root filesystem but resource is busy',
            'Waiting for the next update in the rolling release',
            'Beginning the calculation of PI',
            'The price of bitcoin just went up by 100 USD']
messages_s = ['KERNEL PANIC: watchdog process detected a rogue process. Logging to file',
            'Authorising RPC connection on port ' + str(random.randint(1, 65535)),
            'Detected unauthorised access to port ' + str(random.randint(1, 65535)) + ', sending response payload',
            'KERNEL Soft lockup, CPU stuck for 22s (init - 0)',
            'Fetching update server cache',
            'Rebuilding package management hierarchy',
            'Building initial RAMFS',
            'Booting paravirtualized kernel on bare hardware',
            'Enabling NMI watchdog for all CPUs',
            'Handshaking DHCP server and obtaining local IP address',
            'Obtaining hash table from caching node: 192.168.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)),
            'Setting up secured tunnel to desired transparent proxy',
            'Polling PCI structure for device changes',
            'Handling stack overflow at location ' + hex(random.randint(0xf00000000, 0xfffffffff)),
            'Loading configuration files',
            'Recovering ext4 journal from /dev/sda2']

rows, cols = os.popen('stty size', 'r').read().split()

class window:
    def __init__(self):
        self.win = []
        self.iter = -1
        self.spin_ico = '|/-\\'

    def addln(self, content):
        self.win.append(content)
        if len(self.win) >= int(cols):
            self.win.pop(0)

    def spinner(self):
        self.iter += 1
        if self.iter >= len(self.spin_ico):
            self.iter = -1
        return self.spin_ico[self.iter].rjust(int(cols))

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while len(self.win) < int(rows):
            self.win.append(' ')
        self.win.append(self.spinner())
        for ln in self.win:
            print(ln)
        self.win.pop()

main = window()
prev = None
new = None
while True:
    if round(random.uniform(0, 10)) > 9:
        if argv[1] != None:
            choice = 2
        else:
            choice = random.randint(0, 1)
        if (argv[1] == '-j') or choice == 0:
            while new == prev:
                new = messages_j[random.randint(0, len(messages_j)-1)]
        elif (argv[1] == '-s') or choice == 1:
            while new == prev:
                new = messages_s[random.randint(0, len(messages_s)-1)]
        main.addln('[' + str(format(clock(),'.6f')) + '] ' + new + '...')
        prev = new
    main.display()
    sleep(0.3)

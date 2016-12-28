import commands
import TimetableDat as tt
from operator import xor

global day, hour, minute, weekdef
day = commands.getoutput("date '+%a'")
hour = int(commands.getoutput("date '+%H'"))
minute = int(commands.getoutput("date '+%M'"))
weekdef = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def shift(l):
    return l[1:] + l[:1]

def In_School():
    if day != 'Sat' or day != 'Sun':
        a = True
    if 7 < hour < 15:
        b = True
    try:
        return a and b
    except:
        return False

def Hrs_to_School():
    tmp = weekdef
    #shift until current day is first
    while tmp[0] != day:
        tmp = shift(tmp)
    done = False
    #find the next shool day, i represents how many days away it is
    for i, d in enumerate(tmp):
        if d != 'Fri' or not hour >= 15: #if not friday afternoon
            for schoolDay in weekdef[:5]:
                if d == schoolDay:
                    done = True
                    break
        if done:
            break
    hours = 0
    #calculate days into hours
    hours = hours + max(0, ((i-1) * 24))
    #calculate remaining hours
    if hour >= 15:
        hours = hours + (24 - hour) + 8
    else:
        hours = hours + (8 - hour)
    return str(hours)

if In_School():
    #stuff goes here
    pass
elif tt.Holidays:
    print('School Holidays!')
else:
    print('School in ' + Hrs_to_School() + 'hrs')

'''
To Add:
    - Weekly exceptions with auto cleanup
    - school start and end as variables
    - CL UI for timetable entry
'''

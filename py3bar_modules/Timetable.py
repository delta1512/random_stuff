import commands
import TimetableDat as tt

global day, hour, minute, weekdef, startSchool, endSchool
day = commands.getoutput("date '+%a'")
hour = int(commands.getoutput("date '+%H'"))
minute = int(commands.getoutput("date '+%M'"))
weekdef = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
startSchool = tt.schoolTimes[0]
endSchool = tt.schoolTimes[1]

def shift(l):
    return l[1:] + l[:1]

def In_School():
    if day != 'Sat' or day != 'Sun':
        a = True
    if startSchool-1 < hour < endSchool:
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
        #if not the last school day afternoon
        if d != tt.SchoolDays[len(tt.SchoolDays)-1] or not hour >= endSchool:
            for schoolDay in tt.SchoolDays:
                if d == schoolDay:
                    done = True
                    break
        if done:
            break
    hours = 0
    #calculate days into hours
    hours = hours + max(0, ((i-1) * 24))
    #calculate remaining hours
    if hour >= endSchool:
        hours = hours + (24 - hour) + startSchool
    else:
        hours = hours + (startSchool - hour)
    return str(hours)

'''
def Next_Class(formatClass, formatTime, formatTeacher):
    #set up indeces based on week A or B
    #vvv then collect info using indeces above and changing the final index vvv
    if formatClass:
        pass
    if formatTime:
        pass
    if formatTeacher:
        pass
    return message
'''

if In_School():
    #Next_Class() goes here
    pass
elif tt.Holidays:
    print('School Holidays!')
else:
    print('School in ' + Hrs_to_School() + 'hrs')

'''
To Add:
    - Weekly exceptions with auto cleanup
    - CL UI for timetable entry
'''

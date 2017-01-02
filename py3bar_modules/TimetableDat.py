import commands
#Timetible info
#----------------------------------------
MonA = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

TueA = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

WedA = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

ThuA = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

FriA = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]


MonB = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

TueB = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

WedB = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

ThuB = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

FriB = [['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', ''],

        ['', '', ''],
        ['', '', '']]

timetable = [MonA, TueA, WedA, ThuA, FriA,
             MonB, TueB, WedB, ThuB, FriB]
#----------------------------------------

#Weekly exceptions
#----------------------------------------

#----------------------------------------

#Functions
#----------------------------------------
'''
Get_Week_Info(start):
Get the value of TermStart and count up to the current date,
record amount of weeks and invert the boolean that would represent
week A/B for each week increment. Return: weekletterstring, weeknumber
False = WeekA
True = WeekB
int(commands.getoutput("date '+%m'"))
'''
#----------------------------------------

#Other
#----------------------------------------
Holidays = False
SchoolDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
schoolTimes = [8, 15] #Start and finish hours (24hr)
TermStart = [1, 1] #Starting date (Day/Month)
         # Hr,    Min
PTimes = [['8',  '0' ], #Period 1
          ['8',  '50'], #Period 2
          ['10', '20'], #Period 3
          ['11', '10'], #Period 4
          ['13', '20'], #Period 5
          ['14', '10'], #Period 6
          [str(schoolTimes[1]), '0' ]] #End Time

monthdef = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#CurrentWeekLett, CurrentWeekNum = Get_Week_Info(TermStart)
#----------------------------------------

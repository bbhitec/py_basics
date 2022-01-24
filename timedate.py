# [mst] timedate.py 
# working with dates
# based on the lynda.com 'Learning Python' course
#
# log:
# -dates and times, timedeltas
# -formatting as strings and performing calculations
# -program running time
#

from datetime import date
#from datetime import time
from datetime import datetime
from datetime import timedelta

program_start = datetime.now()  # here we note the program start time

# [demo] DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print ("Today's date is ", today)
today = datetime.now()
print  ("The current date and time is ", today)

# weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)  
# Days start at 0 for Monday 
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print ("Today is day number %d" % wd)
print ("Which is a " + days[wd])

# [demo] Date Formatting
now = datetime.now()
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print (now.strftime("%a, %d %B, %y")) # abbreviated day, num, full month, abbreviated year

# [demo] Time Formatting
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print (now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM


# construct a basic timedelta and print it
print (timedelta(days=365, hours=5, minutes=1))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("one week ago it was " + s)


# [exc] How many days until April Fools' Day?
today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day  
time_to_afd = abs(afd - today)
print (time_to_afd.days, "days until next April Fools' Day!")



# [demo] Calendar construct
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str2 = c.formatmonth(2020, 8, 0, 0)
print (str2)

# # we can iterate through month days. days belonging to adjacent months will be '0'
# for i in c.itermonthdays(2020, 8):
#     print (i)


# [exc] lynda.com - calculate the date of each first friday of each month
# [mst] a bit shortened solution: go through dates and print just the first fridays of the month
# [mst] -from current day on

print ("listing all first Fridays of each month...")
cal = calendar.TextCalendar(calendar.MONDAY)
for month in range(datetime.now().month,13):    
    for i in cal.itermonthdays(2020, month):
        if i!=0:    # [mst] ignore pad-zero-days
            curr_day = date(2020, month, i)
            if date.weekday(curr_day) == days.index("friday"):
                print (curr_day, " day is a Friday")
                break    # this will print just the first Friday of each month



# [demo] various
# enumerate will will zip an index to a list member                
for i, j in enumerate (days):
    print (i, j)

# # [demo] help will list the possible actions over an object    
# help(["foo", "bar", "baz"])


program_runtime =  datetime.now() - program_start #will result in a 'timedelta' object
print ("the program ran for %d ms" % program_runtime.microseconds)
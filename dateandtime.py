"""Python Date and time Tutorial

Python provides the datetime module to work with dates and times effectively. 
Below are the key concepts to understand and master:
"""

"""1.Getting the Current Date and Time
Use the datetime module to fetch the current date and time.
"""
from datetime import datetime
CurrentDate = datetime.now()
print("Current date and time is:", CurrentDate)


''' 2. Formatting Dates (strftime)
      To convert a datetime object into a formatted string, 
      use .strftime()
      
    
'''
FormattedDate = CurrentDate.strftime("%Y-%m-%d %H:%M:%S")
print("formatted date is :",FormattedDate)

"""Common Formatting Codes:
%Y  Year in four digits eg 2025
%y   year in 2 digits  e.g 25
%m   Month   eg 01 indicating January
%d    Day     e.g 20
%A  day of week    eg Sunday
%H   Hour(24 Hour format)   e.g 14
%I   Hour (12 hour format)   eg 02
%p  AM/PM       e.g  PM
%M   Minute(00 -59)   e.g 30
%S    Seconds(00-59)   e.g 30
"""


'''3.Parsing Strings into Dates (strptime)
To convert a string into a datetime object, use strptime()
'''

date_string = "2025-03-16 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("parsed date = ",parsed_date)


'''4.Getting Specific Date Components
Extract year, month,day, hour,minute and second
from a datetime object
'''

print ("Year is: ", CurrentDate.year)
print ("Month is: ", CurrentDate.month)
print ("Day is: ", CurrentDate.day)
print ("Hour is: ", CurrentDate.hour)
print ("Minute is: ", CurrentDate.minute)
print ("Second is: ", CurrentDate.second)



'''5.Working with Dates( date Class)
  Sometimes, you only need the date without the time
  eg
  
''' 

from datetime import date
today = date.today()

print("today's date is :", today)
print("Year :", today.year)
print("Month :", today.month)
print("Day :", today.day)


''' 6. Working with time (Time class)
  The time class represents time without a date
  
'''

from datetime import time 

my_time = time(14,30,15)
print ("The time is :", my_time)
print("Hour: ", my_time.hour)
print("Minute: ", my_time.minute)
print("Second: ", my_time.second)



'''7. Adding and Subtracting Dates (timedelta)
Use timedelta to perform date arithmetic
'''

from datetime import timedelta

# add 10 days

future_date = CurrentDate + timedelta(days=10)
print("Future date is: ", future_date)

# Subtract 7days
previous_date = CurrentDate - timedelta(days = 7)
print("Past date is: ", previous_date)

# Add 2 hours and 30 minutes
new_time = CurrentDate+ timedelta(hours=2, minutes=30)
print("New time is: ", new_time)


'''
Comparing Dates
Python allows comparison of datetime Objects
'''

date1 = datetime(2025,3,10)
date2 = datetime(2025,3,16)

if date1 < date2:
      print("date1 is earlier than date 2")
else:
      print("date1 is later than date2")
      

'''
9. Measuring Execution Time
 To measure how long a function takes, 
 use datetime or the time module
'''

import time

start_time = time.time()


#simulate some processing
time.sleep(2)

end_time =time.time()


execution_time = end_time - start_time

print("Execution Time : ", execution_time, "seconds")


''' 10. Time zones with pytz
Python's datetime module does not handle time zones well, so we use pytz
'''

from datetime import datetime
import pytz

# set timezone
timezone = pytz.timezone("Africa/Lagos")
lagos_time = datetime.now(timezone)
print("Lagos time is: ", lagos_time.strftime("%Y-%m-%d %H:%M:%S %Z"))



# Classwork


todays_date = CurrentDate
print("today's date is ", CurrentDate.strftime("%A, %d %B %Y"))



def Calculate_age(birthyear):      
      today = datetime.today()
      age = today - birthyear
      print("Your age is ", age )
      
Calculate_age(2000)
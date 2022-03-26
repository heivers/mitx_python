import calendar as cal
from datetime import date
from datetime import timedelta


def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[2][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


print("In 2011, US Thanksgiving was on November", find_thanksgiving(2011))

def canadian_thanksgiving(year):
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving


def shopping_days(year):
    """year a number >=1941
    returns the number of days between U.S. Thanksgiving and Christmas in year"""
    thanksgiving = date(year, month=11, day=find_thanksgiving(year))
    canada_thanksgiving = date(year, month=10, day=canadian_thanksgiving(year))
    christmas = date(year, month=12, day=25)
    days_us = christmas - thanksgiving
    days_canada = christmas - canada_thanksgiving
    return days_us, days_canada

print("Number of days between Thanksgiving and Christmas:", shopping_days(2010)[0])
print("Number of days between Canadian Thanksgiving and Christmas:", shopping_days(2010)[1])

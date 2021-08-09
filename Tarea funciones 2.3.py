"""
@author:  Alina Díaz
"""
def isYearLeap(yr):
    if yr%4 == 0 and  yr%100 !=0 or yr%400 == 0:
        return  True
    else:
        return False

def daysInMonth(yr, month):
    if yr<1900 or month>12:
        return None
    if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
        return 31
    elif month==2 and isYearLeap(yr):
        return 29
    else:
        return 28
    
def dayOfYear(yr, month, day):
    diasn=yr,month,day
    if yr<1900 or month>12 or  month<1 or day<1 or day>32:
        return None
    else:
        return diasn

print(dayOfYear(2000, 12, 31))


for x in range(6,2):
  print(x) 
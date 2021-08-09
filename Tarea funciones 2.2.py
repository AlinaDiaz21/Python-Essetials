"""
@author: Alina Díaz
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
testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
                yr = testYears[i]
                mo = testMonths[i]
                print(yr, mo, "->", end="")
                result = daysInMonth(yr, mo)
                if result == testResults[i]:
                                print("OK")
                else:
                                print("Failed")
                            
                            


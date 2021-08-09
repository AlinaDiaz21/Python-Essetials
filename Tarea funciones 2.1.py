"""
@author: Alina
"""
def isYearLeap(yr):
    if yr%4 == 0 and  yr%100 !=0 or yr%400 == 0:
        return  True
    else:
        return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:
                    print("OK")
            else:
                    print("Failed")

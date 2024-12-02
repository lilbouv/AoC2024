# Path: day2/day2.py
# Author: thebo
# Date: 2024-12-01 10:13:47.845306
#
# Problem:
#
# Solution:
#
#
# Part 2
file = open("day2.txt", "r")
lines = file.read().splitlines()
#print(lines)

safe = 0
tolerance = 0
for report in lines:
    report = report.split(" ")
    increase = False
    decrease = False
    bad = False
    for n in range(len(report)-1):
        print(report)
        if int(report[n]) == int(report[n+1]):
            bad = True
            break
        if int(report[n]) - int(report[n+1]) > 3 and int(report[n] )- int(report[n+1]) > 0:
            bad = True
            break
        if int(report[n] )- int(report[n+1]) < -3  and int(report[n] )- int(report[n+1]) < 0:
            bad = True
            break
        if int(report[n] )- int(report[n+1]) < 0:
            if decrease:
                bad = True
                break
            increase = True
        if int(report[n] )- int(report[n+1]) > 0:
            if increase:
                bad = True
                break
            decrease = True
    if not bad:
        safe += 1
    else:
        
        # go through each number and check if it can be removed and if it makes the report good, if so add it to tolerance
        for n in range(len(report)):
            temp = report.copy()
            temp.pop(n)
            increase = False
            decrease = False
            bad = False
            for i in range(len(temp)-1):
                if int(temp[i]) == int(temp[i+1]):
                    bad = True
                    break
                if int(temp[i]) - int(temp[i+1]) > 3 and int(temp[i] )- int(temp[i+1]) > 0:
                    bad = True
                    break
                if int(temp[i] )- int(temp[i+1]) < -3  and int(temp[i] )- int(temp[i+1]) < 0:
                    bad = True
                    break
                if int(temp[i] )- int(temp[i+1]) < 0:
                    if decrease:
                        bad = True
                        break
                    increase = True
                if int(temp[i] )- int(temp[i+1]) > 0:
                    if increase:
                        bad = True
                        break
                    decrease = True
            if not bad:
                tolerance += 1
                break
print(safe)
print(tolerance)
print(safe + tolerance)
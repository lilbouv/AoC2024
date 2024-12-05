# Path: day5/day5.py
# Author: thebo
# Date: 2024-12-01 10:13:47.846309
#
# Problem:
#
# Solution:
#
#
# Part 2
f = open("day5.txt", "r")
lines = f.readlines()
#print(lines, lines.index("\n"))
firstpart = lines[0:lines.index("\n")]
secondpart = lines[lines.index("\n") + 1:]
firstpart = [x.strip() for x in firstpart]
secondpart = [x.strip() for x in secondpart]
#print(firstpart, secondpart)
toCheck = {}
for item in firstpart:
    x,y = item.split("|")
    if x not in toCheck:
        toCheck[x] = [y]
    else:
        toCheck[x].append(y)
s = 0
incorrectlist = []
for u in secondpart:
    print(u)
    isGood = True
    for number in range(len(u.split(","))):
        # all numbers in toCheck for this number cannot appear before this number. Set to false if they appear before. It is okay if they do not appear at all or appear after.
        if u.split(",")[number] in toCheck:
            for item in toCheck[u.split(",")[number]]:
                if item in u.split(",")[0:number]:
                    #print(item, u.split(",")[0:number])

                    isGood = False
                    incorrectlist.append(u.split(","))
                    

        if not isGood:
            break
    if isGood:
        #get the middle number and add it to the sum
        #print("adding", u.split(",")[len(u.split(","))//2])
        s += int(u.split(",")[len(u.split(","))//2])
print(s)

# LOL i should have just randomzied the list and checked if it was good.
while True:
    changed = False
    for item in incorrectlist:
        for number in range(len(item)):
            if item[number] in toCheck:
                for item2 in toCheck[item[number]]:
                    if item2 in item[0:number]:
                        #print("swapping", item[number], item2)
                        item[number], item[item.index(item2)] = item[item.index(item2)], item[number]
                        changed = True
        if changed:
            break
    if not changed:
        break

bsum = 0
for item in incorrectlist:
    bsum += int(item[len(item)//2])
#print(incorrectlist)
print(bsum)
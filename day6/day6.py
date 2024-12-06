f = [x.strip() for x in open("day6.txt", "r").readlines()]

# Part 1

# Read the file and split the input into groups
# Read into 2d array
#print(f)
def getGuardPosition():
    for row in range(len(f)):
        for character in range(len(f[row])):
            if f[row][character] == "^":
                return (row, character)

def calculateAllGuardSpots(x,y, f=f):
    guardPosition = (x,y)
    # Guard will always start by gowing up if it is possible, and will turn right if it is not possible to go up.
    UP = [-1, 0]
    RIGHT = [0, 1]
    DOWN = [1, 0]
    LEFT = [0, -1]

    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
    LAST_MOVE = 0

    # Check last move in file and if it is not a #, move the guard position
    pastGuardPositions = [(guardPosition, LAST_MOVE)]
    while guardPosition[0] > 0 and guardPosition[1] > 0 and guardPosition[0] < len(f) and guardPosition[1] < len(f[0]):
        #if it reaches a previous guard position in the same direction, then it will loop infinitely.
        
        try:
            if f[guardPosition[0] + DIRECTIONS[LAST_MOVE][0]][guardPosition[1] + DIRECTIONS[LAST_MOVE][1]] != "#":
                guardPosition = (guardPosition[0] + DIRECTIONS[LAST_MOVE][0], guardPosition[1] + DIRECTIONS[LAST_MOVE][1])
                if (guardPosition, LAST_MOVE) in pastGuardPositions:
                    return []
                pastGuardPositions.append((guardPosition, LAST_MOVE))
            else:
                LAST_MOVE = (LAST_MOVE + 1) % 4
                guardPosition = (guardPosition[0] + DIRECTIONS[LAST_MOVE][0], guardPosition[1] + DIRECTIONS[LAST_MOVE][1])
                if (guardPosition, LAST_MOVE) in pastGuardPositions:
                    return []
                pastGuardPositions.append((guardPosition, LAST_MOVE))
            
            #print a recreation of the map with the guard position being updated
            # for row in range(len(f)):
            #     for character in range(len(f[row])):
            #         pass
                    # if (row, character) == guardPosition:
                    #     print("^", end="")
                    # else:
                    #     print(f[row][character].replace("^", "."), end="")
                #print()
        except:
            break
    #print distinct guard positions
    #print(len(set([x[0] for x in pastGuardPositions])))
    return pastGuardPositions
    #Next, find the number of distinct places I can place an obstacle to cause the guard to infinitely loop.
    #Check all guard positions and see if placing a wall will cause the guard to loop infinitely
startingPos = getGuardPosition()
previousGuardSpots = calculateAllGuardSpots(startingPos[0], startingPos[1], f)
print("-----------------")
c = 0
c_spot = []
print(len(previousGuardSpots))
check = 0
for spot in previousGuardSpots:
    print("Checking spot", str(check), spot)
    check+=1
    f_new = f.copy()
    f_new[spot[0][0]] = f_new[spot[0][0]][:spot[0][1]] + "#" + f_new[spot[0][0]][spot[0][1]+1:]

    startingPos = getGuardPosition()
    previousGuardSpots = calculateAllGuardSpots(startingPos[0], startingPos[1], f_new)
    if len(previousGuardSpots) == 0:
        c_spot.append(spot)
        c+=1
print(len(list(set([x[0] for x in c_spot]))))


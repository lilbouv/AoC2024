for i in range(len(lines)):
    for c in lines[i]:
        if c == 'X':
            #check any adjacent columns for an M, including diagonals
            #if there is an M, check any adjacent columns for an A, including diagonals and backwards
            #if there is an A, check any adjacent columns for an S, including diagonals and backwards
            print("Found an X", lines[i].index(c))
            adjacentX = [-1, 0, 1]
            adjacentY = [-1, 0, 1]
            for x in adjacentX:
                for y in adjacentY:
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= len(lines):
                        continue
                    if lines[i + x][lines[i].index(c) + y] == 'M':
                        print("Found an M", i + x, lines[i].index(c) + y)
                        for x2 in adjacentX:
                            for y2 in adjacentY:
                                if i + x + x2 < 0 or i + x + x2 >= len(lines):
                                    continue
                                if lines[i + x + x2][lines[i].index(c) + y + y2] == 'A':
                                    print("Found an A", i + x + x2, lines[i].index(c) + y + y2)
                                    for x3 in adjacentX:
                                        for y3 in adjacentY:
                                            if i + x + x2 + x3 < 0 or i + x + x2 + x3 >= len(lines):
                                                continue
                                            if lines[i + x + x2 + x3][lines[i].index(c) + y + y2 + y3] == 'S':
                                                print("Found an S", i + x + x2 + x3, lines[i].index(c) + y + y2 + y3)
                                                count += 1
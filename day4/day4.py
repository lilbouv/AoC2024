f = open("day4.txt", "r")
lines = f.readlines()
f.close()
count = 0
for i in range(len(lines)):
    for c in range(len(lines[i])):
        if lines[i][c] == 'X':
            #check any adjacent columns for an M, including diagonals
            #if there is an M, check any adjacent columns for an A, including diagonals and backwards
            #if there is an A, check any adjacent columns for an S, including diagonals and backwards
            #print("Found an X", lines[i][c])
            #check any adjacent columns for an M, including diagonals
            options = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,1], [-1,0], [-1,-1]]
            for option in options:
                x = option[0]
                y = option[1]
                onlyOption = [[x, y]]
                if i + x < 0 or i + x >= len(lines):  # Row bounds
                    continue
                if c + y < 0 or c + y >= len(lines[i + x]):  # Column bounds for the new row
                    continue
                #print("Found an X", i, c)
                if lines[i + x][c + y] == 'M':
                    #print("Found an M", i + x, lines[i][c] + y)
                    for option2 in onlyOption:
                        x2 = option2[0]
                        y2 = option2[1]
                        if i + x + x2 < 0 or i + x + x2 >= len(lines):
                            continue
                        if lines[i + x + x2][c + y + y2] == 'A':
                            #print("Found an A", i + x + x2, lines[i][c] + y + y2)
                            for option3 in onlyOption:
                                x3 = option3[0]
                                y3 = option3[1]
                                if i + x + x2 + x3 < 0 or i + x + x2 + x3 >= len(lines):
                                    continue
                                if lines[i + x + x2 + x3][c + y + y2 + y3] == 'S':
                                    #print("Found an S", i + x + x2 + x3, lines[i][c] + y + y2 + y3)
                                    #print the coordinates of the X, M, A, and S
                                    # print("X:", i, c)
                                    # print("M:", i + x, c + y)
                                    # print("A:", i + x + x2, c + y + y2)
                                    # print("S:", i + x + x2 + x3, c + y + y2 + y3)
                                    count += 1
print(count)
f = open("day4.txt", "r")
lines = [line.strip() for line in f.readlines()]
f.close()

count = 0

for i in range(1, len(lines) - 1):  # Avoid edges
    for j in range(1, len(lines[i]) - 1):  # Avoid edges
        if lines[i][j] == 'A':  # Center of the "X"
            options = [[-1, -1], [-1, 1], [1, -1], [1, 1]]  # Diagonal directions
            diagonals = []

            for option in options:
                x, y = option
                if 0 <= i + x < len(lines) and 0 <= j + y < len(lines[i + x]):
                    diagonals.append((i + x, j + y))

            if len(diagonals) == 4:
                # Check pairs of opposite diagonal elements for M and S
                if (
                    ((lines[diagonals[0][0]][diagonals[0][1]] == 'M' and lines[diagonals[3][0]][diagonals[3][1]] == 'S') or
                     (lines[diagonals[0][0]][diagonals[0][1]] == 'S' and lines[diagonals[3][0]][diagonals[3][1]] == 'M')) and
                    ((lines[diagonals[1][0]][diagonals[1][1]] == 'M' and lines[diagonals[2][0]][diagonals[2][1]] == 'S') or
                     (lines[diagonals[1][0]][diagonals[1][1]] == 'S' and lines[diagonals[2][0]][diagonals[2][1]] == 'M'))
                ):
                    count += 1

print(count)

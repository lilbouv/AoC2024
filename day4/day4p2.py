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

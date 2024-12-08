f = open("day8.txt", "r")
lines = [x.strip() for x in f.readlines()]
bounds = (len(lines), len(lines[0]))
print(bounds)
d = {}
for line in range(len(lines)):
    for c in range(len(lines[line])):
        if lines[line][c] != ".":
            if lines[line][c] not in d:
                d[lines[line][c]] = [(line, c)]
            else:
                d[lines[line][c]].append((line, c))
#create permutations of all possible pairs of points in each letter of the dict. 

from itertools import combinations
for key in d:
    d[key] = list(combinations(d[key], 2))

def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return "inf"
    return  (p2[0] - p1[0]), (p2[1] - p1[1])

nodes = []
for key in d:
    for pair in d[key]:
        slope = get_slope(pair[0], pair[1])
        print(key, pair, slope)
        new_pairs = ((pair[0][0] + slope[0]*2, pair[0][1] + slope[1]*2), (pair[0][0] - slope[0], pair[0][1] - slope[1]))
        for pair in new_pairs:
            if pair[0] >= 0 and pair[0] < bounds[0] and pair[1] >= 0 and pair[1] < bounds[1]:
                nodes.append(pair)
print("Part 1: ", len(list(set(nodes))))
# Part 2
def get_all_pairs(p1, slope, bounds):
    pairs = []
    for i in range(-1*bounds[0], bounds[0]+1):
        new_pair = (p1[0] + slope[0]*i, p1[1] + slope[1]*i)
        #print(new_pair)
        if new_pair[0] >= 0 and new_pair[0] < bounds[0] and new_pair[1] >= 0 and new_pair[1] < bounds[1]:
            pairs.append(new_pair)
    print("Pairs: ", pairs)
    return pairs
c = []
for key in d:
    for pair in d[key]:
        slope = get_slope(pair[0], pair[1])
        print(key, pair, slope)        
        #generate all new pairs that fit in the bounds
        new_pairs = get_all_pairs(pair[0], slope, bounds)
        for pair in new_pairs:
            if pair not in c:
                c.append(pair)
print("Part 2: ", len(c))
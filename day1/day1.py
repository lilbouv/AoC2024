file = "day1.txt"
with open(file) as f:
    content = f.readlines()
content = [x.strip() for x in content]

l = []
r = []

for line in content:
    line = line.split("   ")
    #print(line)
    l.append(int(line[0]))
    r.append(int(line[1]))
print(l,r)
l = sorted(l)
r = sorted(r)

score = 0
for i in range(len(l)):
    score = abs(l[i] - r[i]) + score
print(score)


# Part 2
score = 0
for i in range(len(l)):
    score = l[i]*r.count(l[i]) + score
print(score) 
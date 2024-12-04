import re

file = open("day3.txt", "r")

lines = file.read()

p1 = 0
for i in re.findall(r'mul\(\d+,\d+\)', lines):
    i = [int(x) for x in i.replace("mul(","").replace(")","").split(",")]
    p1 += (i[0] * i[1])
print(p1)

lines = "do()"+lines #its on by default so just make it do first XD?
p2 = re.findall(r'do\((.*?)don\'t\(\)', lines, re.DOTALL)
p2 = [re.findall(r'mul\(\d+,\d+\)', x) for x in p2]
p2 = [item for sublist in p2 for item in sublist]
p2 = [[int(x) for x in i.replace("mul(","").replace(")","").split(",")] for i in p2]
p2 = [i[0] * i[1] for i in p2]
print(sum(p2))
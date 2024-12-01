import os
import sys
import datetime

#Create folder day2 through day25

for i in range(2, 26):
    folder = "day" + str(i)
    os.mkdir(folder)
    file = folder + "/day" + str(i) + ".py"
    with open(file, "w") as f:
        f.write("# Path: " + file + "\n")
        f.write("# Author: " + os.getlogin() + "\n")
        f.write("# Date: " + str(datetime.datetime.now()) + "\n")
        f.write("#\n")
        f.write("# Problem:\n")
        f.write("#\n")
        f.write("# Solution:\n")
        f.write("#\n")
        f.write("#\n")
        f.write("# Part 2\n")
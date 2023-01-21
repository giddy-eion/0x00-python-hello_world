#!/usr/bin/python3
for comb in range(0, 100):
    if (comb == 99):
        print("{}".format(int(comb)))
    else:
        print("{:02}".format(int(comb)), end=", ")

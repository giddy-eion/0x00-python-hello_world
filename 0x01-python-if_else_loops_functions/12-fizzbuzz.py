#!/usr/bin/python3
def fizzbuzz():
    for multis in range(1, 101):
        if multis % 3 == 0 and multis % 5 == 0:
            print("FizzBuzz ", end="")
        elif multis % 3 == 0:
            print("Fizz ", end="")
        elif multis % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(int(multis)), end="")

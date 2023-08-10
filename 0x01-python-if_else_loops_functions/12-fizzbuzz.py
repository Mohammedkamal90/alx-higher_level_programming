#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print number from 1 to 100 separate with space.

    For multiples three, print Fizz instead of number.
    For multiples five, print Buzz instead of number.
    For multiples three and five, print FizzBuzz instead of number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

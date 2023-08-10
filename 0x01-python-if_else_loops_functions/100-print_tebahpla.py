#!/usr/bin/python3
#100-print_tebahpla.py

""""Print alphabet in reverse order alternating upper- and lower_case."""
x = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - x)), end="")
    x = 32 if x == 0 else 0


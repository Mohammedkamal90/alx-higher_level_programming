#!/usr/bin/python3
# 2-print_alphabet.py

"""Print alphabet in lowercase, not follow with new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")

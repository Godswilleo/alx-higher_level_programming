#!/usr/bin/python3

for num in range(100):
    if (num < 10):
        insert = 0

    else:
        insert = ""

    if (num != 99):
        print(f"{insert}{num}, ", end="")

    else:
        print(f"{num}")

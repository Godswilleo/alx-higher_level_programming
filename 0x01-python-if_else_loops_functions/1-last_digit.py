#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_number = number_str[-1]
l_num_int = int(last_number)

if (l_num_int > 5):
    print(f"Last digit of {number} is {l_num_int} and is greater than 5", end="")

elif (l_num_int == 0):
    print(f"Last digit of {number} is {l_num_int} and is 0")

else:
    last_line = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {l_num_int} {last_line}")

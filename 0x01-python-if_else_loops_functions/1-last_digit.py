#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
s1 = "and is greater than 5"
s2 = "and is less than 6 and not 0"
s3 = "and is 0"
s4 = f"Last digit of {number} is {l} "
if number > 5:
    print(f"{s4}{s1}")
elif number < 6:
    print(f"{s4}{s2}")
else:
    print(f"{s4}{s3}")    

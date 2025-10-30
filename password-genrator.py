# pip install random

import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbol = "!@#$%^&*+"

all = lower + upper + number + symbol
length = int(input("Enter the length of password : "))

password = "".join(random.sample(all, length))
print("password:", password)

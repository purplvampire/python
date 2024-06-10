#! python3
"""
This is a tool for generator password with your custom.
"""
import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "`~!@#$%^&*()-_=+[]{}\|;:'\",.<>/?"

all_chars = lower + upper + numbers + symbols
length = int(input("Enter a length for your password: "))

password = "".join(random.sample(all_chars, length))
print("Generated Password: ", password)
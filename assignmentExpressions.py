#! python3
# Assignment Expressions
# ----------------------------------------------------------------
# 海象运算符

# 用途一: While loop
n = 0
while n < 3:
    print(n)    # 0,1,2
    n = n + 1

# After
w = 0
while (w := w + 1) < 3:
    print(w)    # 1,2

# Sample2
while True:
    p = input("Enter the password:")
    if p == "the password":
        break

# After
while (p := input("Enter the password:")) != "the password":
    continue

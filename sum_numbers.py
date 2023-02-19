#! python3
# Ｕnit29: 只加總資料中的數字

# 範例：ListCompression
print([x ** 2 for x in range(10) if x % 2 == 0])

print([
    x ** 2              # 運算式
    for x in range(10)  # 走訪
    if x % 2 == 0       # 條件式
    ])

# 函式
def sum_numbers(data):
    return sum([
        int(d)
        for d in data.split()
        if d.isdigit()
    ])

print(sum_numbers('10 adb 20 de44 30 55fg 40'))

# 進階版：map(func, args) + filter(func, args) P.7-8
def sum_numbers(data):
    return sum(list(map(int, filter(lambda d: d.isdigit(), data.split()))))

print(sum_numbers('10 adb 20 de44 30 55fg 40'))
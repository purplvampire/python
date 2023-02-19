#! python3
# Unit28:輸出一組數字的絕對值
def abs_numbers(numbers):
    return [abs(x) for x in numbers]    # ListCompresseion(P.7-4)

print(abs_numbers([1, 2, -3, -4, 5]))

# 進階版：map()
def abs_numbers(numbers):
    return list(map(abs, numbers))   # map(func, args) and type transfer.(P.7-5)

print(abs_numbers([1, 2, -3, -4, 5]))
#! python3
# Ｕnit30: 將二維清單壓平成一維清單

# 範例：
my_list = []
for x in [[1, 2], [3, 4]]:
    for y in x:
        my_list.append(y)

print(my_list)

print([
    y                           # 回傳值
    for x in [[1, 2], [3, 4]]   # 迴圈1
        for y in x              # 迴圈2
])

# 函式
def flatten(data):
    return [sub_element
        for element in data
            for sub_element in element  
    ]

print(flatten([[1, 2], [3, 4]]))
# Learning first-class
# 範例
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

# 將operator設為function
def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 5, operator=divide)
print(result)

# 實務應用:查個資
def search(sequence, expected, finder):
    for elem in sequence:
        # 遍尋dict["key"]=value
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    # dict["key"] = value
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))


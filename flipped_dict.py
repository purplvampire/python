#! python3
# 練習dict生成式：{運算式, 運算式 for key, value in 容器}
# 用生成式顛倒其鍵值對後回傳

def flipped_dict(input_dict):
    return {value: key for key, value in input_dict.items()}    # dict.items()回傳tuple(key, value)

print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))

# 延伸技巧

def flipped_dict(input_dict):
    return {input_dict[key]: key for key in input_dict}    # dict不帶函式預設取出key

print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))



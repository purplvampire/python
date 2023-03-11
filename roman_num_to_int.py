#! python3
# A-10:羅馬數字轉正整數

# 解法一:
def roman_num_to_int(roman_num):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    prev_char = None
    for char in roman_num:
        num += roman_dict[char]
        if prev_char != None and roman_dict[char] > prev_char:
            num -= prev_char * 2
        prev_char = roman_dict[char]
    
    return num
print('正整數為', roman_num_to_int('XIX'))

# 範例二:
def roman_num_to_int2(roman_num):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_special = {
        'IV': -2,
        'IX': -2,
        'XL': -20,
        'XC': -20,
        'CD': -200,
        'CM': -200
    }
    normal_value = sum([roman_dict[char] for char in roman_num if char in roman_dict])
    special_value = sum([value for key, value in roman_special.items() if key in roman_num])

    return normal_value + special_value

print(roman_num_to_int2('XIX'))
    
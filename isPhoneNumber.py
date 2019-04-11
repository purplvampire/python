def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False 
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12] # 尋找一段12字元的字串存成變數chunk
    if isPhoneNumber(chunk):# 若檢查結果回傳的值為True則列印出該12個字元變數的值
        print('Phone number found: ' + chunk)
print('Done')

# 使用正規表示式


import re   # 載入模組 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # 用原始字串建立篩選
mo = phoneNumRegex.search('My number is 415-555-4242.')  # 輸入字串查詢
if mo != None:  # 若查詢的結果不是None
    print('Phone number found: ' + mo.group())  # 用group函式返回查詢的值
else:
    print('Phone number found: None')   # 否則回傳沒有


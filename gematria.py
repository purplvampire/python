#! python3
# Unit35：希伯來數字密碼轉換
import string

# 用dictCompression生成希伯來密碼表{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5...}
def gematria_dict():
    return {char: index 
            for index, char 
            in enumerate(string.ascii_lowercase, 1)}    # 字串索引值由1開始, 預設0

GEMATRIA = gematria_dict()

# 計算單字的希伯來數值
def gematria_value(word):
    return sum(GEMATRIA[char] 
                for char in word.lower()    # 字要轉成小寫
                if char in GEMATRIA)        # 字母要有在對照表才計算加總

# 找出文字檔中和指定單字數值相同的單字
def gematria_equal_words(input_word, filename):
    input_value = gematria_value(input_word)            # 指定單字的數值
    with open(filename, 'r', encoding='utf-8') as f:    # 將cp950編碼轉成utf-8
        return [word 
                for line in f
                for word in line.lower().split()        # 將整行字串轉成小寫並切割
                if input_value == gematria_value(word)] # 比對檔案單字與指定單字的數值是否相等

result = gematria_equal_words('programming', r'Alice’s Adventures in Wonderland.txt')
print(result)

print(gematria_value('programming'))
print(gematria_value('puzzling'))
print(gematria_value('distributed'))


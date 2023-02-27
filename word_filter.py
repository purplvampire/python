#! python3
# 過濾檔案中至少有三個母音的單字
# 練習交集/聯集/差集/對稱差集的用法與ListCompression


def word_filter(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as f:
        words = ([word.replace('.', '')     # 字元處理
        for line in f                       # 第1輪ListCompression
        for word in line.strip().split()    # 第2輪ListCompression
        if len(vowels & set(word)) >= 3])   # 2的條件式, 用交集判斷
    
    return words                            # 回傳清單

print(word_filter('text2.txt'))
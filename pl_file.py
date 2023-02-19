#! python3
# 檔案翻譯機

# 豬拉丁文
def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

# 將檔案改造成豬拉丁文
def pl_file(filename):
    with open(filename, 'r') as f:
        return ' '.join([                           # 將所有字合併成字串並以空格分開 
            pl_word(word.lower().replace('.', ''))  # 運算式
                for line in f                       # 迴圈1
                    for word in line.split()        # 迴圈2
            ])


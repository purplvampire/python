#! python3
# 自訂密碼產生器
import random

# 範例
for _ in range(5):
    print(random.choice('0123456789'))

# 函式
def set_password_source(source):
    # 閉包：控制密碼長度
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))    # 帶入父函式參數
        return ''.join(output)
    return password_gen                             # 回傳閉包值

my_password_gen = set_password_source('0123456789@zxcvbnmasdfghjklqwertyuiop')
print(my_password_gen(10))
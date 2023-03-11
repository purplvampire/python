#! python3
# A-9:反轉位元, 將一個介於0~255正整數,轉成8bit的二進位數(00000000),反轉排列順序,再轉回正整數

def reverse_binary(n):
    binary = f'{n:08b}'         # 轉成8位元的二進位(b=binary)
    print('二進位',binary)
    return int(binary[::-1], 2) # 用int(String, 進位數)轉回整數
                                # 用string[::-1]倒轉字串

print('正整數',reverse_binary(121))


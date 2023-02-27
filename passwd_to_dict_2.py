#! python3
# 用DictCompression整理帳密資訊
# 抽出/etc/passwd中的使用者名稱與ID, 包成字典回傳

def passwd_to_dict_2(filename):
    with open(filename) as f:
        d = {words[0]: words[2]
        for words in 
        [line.split(":") for line in f]}
    
    return d

print(passwd_to_dict_2('passwd.cfg'))
# 補充說明
# 影片中我將參數形容成投幣孔，
# 所以例如這個function

def add(x, y):
    print(x + y)

add(3, 4)
"""
我會說把3投到x這個參數，把4投到y這個參數。
術語上，所謂的"投"，是"傳遞"。
所以嚴格術語說法會是，把3傳遞到x參，數把4傳遞到y參數。
這個"傳遞"也是從英文直翻過來的，英文上都是講"pass in"
就是把東西傳遞(pass in)到function內部的概念。

# ------------------------------

另外，
盡量把程式碼寫成function的好處：

1. 收納，程式碼有較良好/明顯的架構
2. 增加重複使用性
3. 也因為以上的原因，寫成function其實大大的降低了debug(除錯)的時間。
程式出錯時，會依照function的執行流程印出來，告訴你哪個function中執行了哪個function，最後在哪個function的第幾行當掉，所以我們可以依照這樣有用的資訊，到出錯的function去看為什麼出錯，又因為我們的function有依照良好的中心思想(功能單一/簡潔)去寫，所以一下子就可以成功除錯。

寫成function，在除錯時，我們是一小段一小段的看程式碼，看看我們的function有沒有設計錯誤。
如果程式沒有寫成function，我們會像無頭蒼蠅，一堆東西不知道是在哪裏宣告的，
哪裡改變成什麼，上下上下查找，大幅增加了除錯的時間。
這樣大家應該有所體會了! 
所以function算是寫程式裡面非常重要的概念!
"""

# ------------------------
# 大致上可以把function視為有四種難度

# 最簡單
def wash():
    print('加水')
    print('加洗衣精')
    print('旋轉')

wash()

# 第二難度:  參數parameter
def wash(dry):
    print('加水')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘乾')

wash(True)
wash(False)

# 第三難度:  多個參數parameter
def wash(dry, water):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘乾')

wash(True, 8)
wash(False, 6)

# 第四難度:  參數parameter 預設值
def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘乾')

wash(water=10) # 只設定一個參數


# -------------------------------

# 彭彭老師課程說明補充：
# 1.無限/不定參數:導出平均值
def avg(*numbers):
    sum = 0
    for num in numbers: # 將無限/不定參數的Tuple值列出
        sum += num      # 將Tuple值相加
    print(int(sum / len(numbers)))  # 印出整數平均值(加總/Tuple長度)
    return int(sum / len(numbers))  # 回傳值
avg(1, 5, 6)

# 2.回傳值:函式執行完畢預設在最後執行 return None，表示回傳None值，
# 若需要將函式的計算結果存成變數使用，需要設定回傳值，舉例如下：
def sayHello(msg):
    return msg      # 回傳msg參數
x = sayHello('Hello')
print(x)

# 3.預設參數:設定平方數
def square(base, exp=0):
    print(base**exp)
square(5)

# 4.變更參數順序:整除
def divide(n1, n2):
    print(n1/n2)
divide(2, 4)
divide(n2=2, n1=4)
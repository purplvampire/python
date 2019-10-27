# 實體物件設計
class OpenFile:
    # 初始化函式
    def __init__(self, filename):
        # 建立實體屬性
        self.file = None        # 初始化檔案為空檔案
        self.filename = filename
        self.read = None        # 初始化檔案為空檔案
    # 實體方法
    def open(self):
        self.file = open(self.filename, mode='r', encoding='utf-8') # 打開文件
        self.read = self.file.read()    # 讀取文件
        self.file.close()               # 關閉文件
        return self.read                # 回傳值

# 建立實體物件
file = OpenFile('hello.txt')

# 將實體物件的實體方法所產生的回傳值存到x變數
x = file.open()

# 列印變數
print(x)
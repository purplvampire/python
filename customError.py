# Learning how to custom errorValue.
# 建立錯誤物件(繼承)
class TooManyPagesReadError(ValueError):
    pass

# 創造書本藍圖
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    
    # 閱讀頁數
    def read(self, pages: int):
        # Debug處理
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        # 頁數加總
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

# 建立書本物件
python101 = Book("Python 101", 50)

# 錯誤處理
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)

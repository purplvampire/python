# 學習物件導向
# 設定物件藍圖
class Student:
    # 初始化物件與參數值
    def __init__(self, name, grades):
        # 物件屬性與參數設定
        self.name = name
        self.grades = grades
    
    # 設定Method
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    # 物件說明
    def __str__(self):
        return f"Person {self.name}, {self.grades} every grade."
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.grades})>"

# 建立物件
student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))

print(student.name)
print(student2.name)
print(student.average_grade())
print(student2.average_grade())
print(student)
print(student.__repr__())

# classmethod: 用來加工處理預設參數, 再回填到物件參數中
# staticmethod: 用來當作一個固定輸出功能,不處理填入參數值
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book(Name '{self.name}', Type '{self.book_type}', Weight {self.weight}g)>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

    @staticmethod
    def static_method():
        print("Called static_method.")

# 指定預設參數與屬性
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
# <Book(Name 'Harry Potter', Type 'hardcover', Weight 1600g)>
print(light)
# <Book(Name 'Python 101', Type 'paperback', Weight 600g)>

# 呼叫staticmethod
book.static_method()



# 物件繼承
print("-----Object inheritance-----")

# 建立裝置物件
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected = False
        print("Disconnected.")

printer = Device("Printer", "USB")
print(printer)
printer.disconnected()

print("-----Printer Object-----")
# 建立印表機物件
class Printer(Device):  # 套用父系物件
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)    # 用super()繼承父系物件
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining.)"
    
    def print(self, pages):
        if not self.connected:  # 已繼承可直接使用父系物件的method
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages   # 減去已使用的紙張數

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()
printer.print(10)


print("-----Object Composition-----")
# 物件的合成
# 建立書架藍圖
class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

# 建立書本藍圖
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

# 建立書本
book = Book("Harry Potter")
book2 = Book("Python 101")

# 建立書架並放入書本
shelf = BookShelf(book, book2)
print(shelf)

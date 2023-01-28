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

# 指定預設參數與屬性
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
# <Book(Name 'Harry Potter', Type 'hardcover', Weight 1600g)>
print(light)
# <Book(Name 'Python 101', Type 'paperback', Weight 600g)>
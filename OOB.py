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
    
    # 物件藍圖說明
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

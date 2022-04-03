#! python3
""" Understanding staticmethod and classmethod

@staticmethod：讓不需要用到屬性的函式以函式的形式執行

@classmethod：讓需要用到屬性的函式可以用函式的形式執行

"""

# 範例

class Batman:
    def __init__(self, hp):
        self.hp = hp

    @staticmethod
    def f():
        print('static method')

    @staticmethod
    def calc_avg(x):
        return sum(x) / len(x)

    # 暫時建立實體物件，所以函式參數用cls，注意要放參數進去
    @classmethod
    def ffff(cls):
        cls(100).f()

# 以函式的形式執行，不用建立實體物件
Batman.f()

x = [1, 2, 3]
print(Batman.calc_avg(x))

Batman.ffff()


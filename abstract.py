#! python3
# Import abstract base class module
from abc import ABCMeta, abstractmethod, ABC

# 建立抽象class
class Product(ABC):
    @abstractmethod
    def hi(self):
        pass

    @abstractmethod
    def hi2(self):
        pass

# 繼承抽象class與抽象method
class Drink(Product):
    def hi(self):
        print('hi')

    def hi2(self):
        print('hi2')

d = Drink()
d.hi()
d.hi2()

### 範例

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Won')

class Cat(Animal):
    def make_sound(self):
        print('Meum')

class Human(Animal):
    def make_sound(self):
        print('Hi')

d = Dog()
d.make_sound()

c = Cat()
c.make_sound()

h = Human()
h.make_sound()


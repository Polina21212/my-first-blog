'''class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Person("Tom", 22)


print(tom.name)
print(tom.age)'''

'''class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Person("Tom", 22)
bob = Person("Bob", 43)

print(tom.name)
print(tom.age)
print(bob.name)
print(bob.age)'''


'''class Calculator:

    def __add__(self, a, b):
        return a + b

    def __multiply__(self, a, b):
        return a * b

calc = Calculator()
print(calc.__add__(2, 3))
print(calc.__multiply__(4, 5))'''


'''class Person:
    def say_hello(self):
        print("Hello")

tom = Person()
tom.say_hello()'''


'''class Person:

    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)

    def __del__(self):
        print("Удален человек с именем", self.name)

def create_person():
    tom = Person("Tom")

create_person()
print("Конец программы")'''


'''class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self. length = l

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

rect1 = Rectangle(40, 40)
print("rect1 area: ", rect1.area())
print("rect1 perimeter: ", rect1.perimeter())

rect2 = Rectangle(20, 20)
print("rect2 area: ", rect2.area())
print("rect2 peremeter: ", rect2.perimeter())'''


class BankAccount:

    def __init__(self, number, sum):
        self.number = number
        self.balance = sum
        print(f"Создан счет. Начальный баланс: {sum} едениц")

    def __add__(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} едениц")

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum} едениц")
        else:
            print("Недостаточно средств")

acc1 = BankAccount("123456577", 1000)
acc1.__add__(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)
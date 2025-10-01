'''n= int(input("Введите количесвто элементов списка: "))
a = []
for i in range(n):
  n = int(input(f"Введите число {i+1}: "))
  a.append(n)
print("Ваш список ",a)
S = 0
numbers = [0]
for j in range(n):
    S += a[j]
print("Сумма чисел вашего списка: ",S)'''
from mypractic.PR7 import message

'''b = 0
while True:
    x = int(input("Введите число (0 - стоп): "))
    if (x == 0):
        break
    b += 1
print("Сколько раз: ",b)'''

'''a = int(input("Введите число: "))
print(a // 10)
print(a % 10)'''

a= input("Введите число: ")
b = input("ведите цифру, которую нужно найти: ")
count = 0
for i in a:
    if i == 0
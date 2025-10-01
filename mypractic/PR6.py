'''num = int(input("Введите число:"))

S = 0
for i in range(1, num + 1):
    S += 1
    if i < num:
      print(i, end= "+")
else:
      print(i, end= " ")
'''
from mimetypes import guess_extension

'''min = int(input("Введите количество минут: "))

hours = min // 60
min = min % 60
print(f"{hours} час и {min} минут")'''

while True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Сума чисел: ", num1 + num2)

    str = input("Нажмите Y или y для завершения программы: ")

    if(str == "Y" or str == "y"):   break


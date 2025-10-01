from django.template.defaultfilters import first
'''print(7 / 2)
print(7 // 2)
print(6 ** 2)
print(7 % 2)
number = 3 + 4 * 5 ** 2 + 7

number = 10
number += 5
print(number)

first_number = 2.001
second_nimber = 0.1
third_nimber = first_number + second_nimber
print(round(third_nimber))
'''

'''language = "russian"
if language == "english":
    print("Hello")
else:
    print("Привет")
print("End")

language = "english"
daytime = "morning"
if language == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
'''
'''number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")
'''

'''message = "Hello"

for a in message:
    print(a)'''

'''for n in range(10):
    print(n, end=" ")'''

'''i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1'''

'''for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")'''

'''while True:
    num1 = int(input("Введите первое число: "))

    num2 = int(input("Введите второе число: "))

    print("Сумма чисел: ", num1+num2 )

    str = input ("Нажмите Y или y для завершения программы: ")

    if (str =="Y" or str =="y"):  break
'''
'''n = 7
for i in range(0, n):
    for j in range(0, n):
        if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
        else: print(" ", end="")
    print()
'''

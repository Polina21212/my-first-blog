n = int(input("Введите количество элментов списка: "))
nums = []
for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    nums.append(num)
    print("Все числа: ", nums)
print("Сумма чисел:", sum(nums))
print("Среднее арифметическое:",sum(nums) // len(nums))
print("Минимальное значение: ", min(nums))
print("Максимальное значение: ", max(nums))
b = 0
c = 0
for x in nums:
    if x < 0:
        b +=1
        c+=1
        print("Отрицательные числа: ")
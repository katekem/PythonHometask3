# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
num = int(input('Введите число: '))

res = []
i = 0
while num // 2 != 0:
    res.append(num%2)
    num //= 2
res.append(num)

res = res[::-1]
res = [str(x) for x in res]
res = ''.join(res)
print(f'Это число в двоичном коде = {res}')


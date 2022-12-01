# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число: '))

my_list = []
for i in range(k):
    if i == 0 or i == 1:
        my_list.append(1)
    else:
        my_list.append(my_list[i-1] + my_list[i-2])

new_list = my_list[:]

for i in range(k+1):
    if i == 0:
        new_list.insert(0,0)
    else:
        if i % 2 == 0:
            new_list.insert(0,-my_list[i-1])
        else:
            new_list.insert(0,my_list[i-1])

print(new_list)


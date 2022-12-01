# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random as rnd
my_list = [round(rnd.uniform(0,10),2) for _ in range(0,5)]
print(my_list)

temp = 0
new_list = []
for i in my_list:
    if i != int(i):
        temp = str(i).split('.')
        new_list.append(temp[1])

new_list = [int(x) for x in new_list]

min = new_list[0]
max = new_list[0]
for i in new_list:
    if i<min:
        min = i
    if i > max: max = i

diff = max - min

print(f'Разница между дробными частями min = {min} и max = {max} = {diff}')
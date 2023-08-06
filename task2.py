# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]

def indexfind(list1, a, b):
   index = list()
   for i in range(len(list1)):
      if a<=list1[i]<=b:
         index.append(i)
   return index
from random import randint
list1 = [randint(0,10) for i in range(10)]
print('исходный массив: ')
print(list1)
a = int(input('введите минимум поиска: '))
b = int(input('введите максимум поиска: '))
print(f'индексы элементов, значения которых в диапазоне [{a}, {b}]: {indexfind(list1, a, b)}')
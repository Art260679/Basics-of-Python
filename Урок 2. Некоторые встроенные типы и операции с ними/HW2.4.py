"""5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
B. Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""
from copy import copy


list1 = [346.17, 651.57, 330.23, 298.42, 662.99, 62.69, 121.88, 504.39, 879.56, 322.4, 481.87, 481.78, 58.42, 359.55,
         388.27, 595.41, 548.62, 371.08, 594.01, 709.85]

# A
for i in list1:
    print(f'{str(i).split(".")[0]} руб {(str(i).split("."))[1].zfill(2)} коп', end=', ')
print('\n')
print(f'ID до сортировки {id(list1)}')

# B
print('\n\n')
list1.sort()
for i in list1:
    print(f'{str(i).split(".")[0]} руб {(str(i).split("."))[1].zfill(2)} коп', end=', ')
print('\n')
print(f'ID после сортировки {id(list1)}')

# C
print('\n')
list2 = copy(list1)
list2.sort(reverse=True)
print(list2)
print(f'ID после копирования {id(list2)}')

# D
print(f'\nПять самых дорогих товаров: {list2[:6]}')

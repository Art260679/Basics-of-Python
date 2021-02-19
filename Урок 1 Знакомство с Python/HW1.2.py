"""2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
 сумма цифр которых делится нацело на 7.
 Внимание: новый список не создавать!!!"""

# Создадим список
lst = []
for i in range(1000):
    if i % 2:
        lst.append(i ** 3)
s = 0
s2 = 0
# Разобъем каждое составное число на отдельные числа и сложим их
for i in lst:
    n = list(str(i))
    num = 0
    for j in n:
        num += int(j)
    # найдем сумму чисел, которые делятся на 7 без остатка
    if num % 7 == 0:
        s += num
print(s)
# К каждому числу списка прибавим 17
for i in range(len(lst)):
    lst[i] += 17
# Разобъем каждое составное число на отдельные числа и сложим их
for i in lst:
    n = list(str(i))
    num2 = 0
    # найдем сумму чисел, которые делятся на 7 без остатка
    for j in n:
        num2 += int(j)
    if num2 % 7 == 0:
        s2 += num2
print(s2)

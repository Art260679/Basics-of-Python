"""3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки. """

meaning = int(input('Введите число от 1 до 20: '))

if 2 <= meaning <= 4:
    print(f'{meaning} процента')
elif meaning == 1:
    print(f'{meaning} процент')
else:
    print(f'{meaning} процентов')
print('-' * 20)
# Вывести все склонения для проверки
for i in range(20):
    if 2 <= i <= 4:
        print(f'{i} процента')
    elif i == 1:
        print(f'{i} процент')
    else:
        print(f'{i} процентов')

# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.


def is_year_leap(y):
    """
    Функция проверяет высокосный год.

    :param y: Вводимый год
    :return:
    """
    if 1582 > y >= 8 and y % 4 == 0:
        return True
    elif y >= 1582 and y % 400 == 0:
        return True
    elif y >= 1582 and y % 100 == 0:
        return False
    elif y >= 1582 and y % 4 == 0:
        return True
    elif -45 <= y < 8 and y % 3 == 0:
        return True
    elif y < -45:
        return '(!) Первым високосным годом стал 45 год до н. э.'


y = int(input('\nВведите год ("-", если год д.н.э.): '))
res = is_year_leap(y)

if y < -45:
    print('\n\t(!) Первым високосным годом стал 45 год до н. э.')
elif res:
    print('\n\t{} год - высокосный.'.format(y))
elif not res:
    print('\n\t{} год - невисокосный.'.format(y))


'''
Из сопоставления римских и египетских датировок по оксиринхскому папирусу, опубликованному в 1999 году, 
было установлено, что високосными годами в Риме были 
42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9 годы до н. э., 
8, 12 годы н. э. и в последующем каждый четвёртый год.

В 1582 году римский папа Григорий XIII провёл реформу календаря. 
Чтобы средний календарный год лучше соответствовал солнечному, было решено изменить правило високосных лет. 
По-прежнему високосным оставался год, номер которого кратен четырём, но исключение делалось для тех, 
которые были кратны 100. Такие годы были високосными только тогда, когда делились ещё и на 400.

Отсюда следует распределение високосных годов:

год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные (например, го­ды 1700, 1800, 1900, 2100);
остальные годы, номер которых кратен 4, — високосные.
Таким образом, григорианский календарь значительно точнее юлианского, но всё равно не лишён недостатков.
'''
# Дана строка.
# Найти нижеописанные срезы.

s = str(input('\n\t\tВведите строку:\t'))
print('\n\tСтрока: ', s, '\n')
print('a. третий символ этой строки:\t\t\t\t', s[3])
print('b. предпоследний символ этой строки:\t\t', s[-2])
print('c. первые пять символов этой строки:\t\t', s[:5])
print('d. кроме последних двух символов:\t\t\t', s[:-2:])
print('e. все символы с четными индексами:\t\t\t', s[::2])
print('f. символы с нечетными индексами:\t\t\t', s[1::2])
print('g. все символы в обратном порядке:\t\t\t', s[::-1])
print('h. все символы строки через один в\n\tобратном порядке, начиная с последнего:\t', s[::-2])
print('g. длина данной строки:\t\t\t\t\t\t', len(s))
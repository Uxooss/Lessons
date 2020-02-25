# В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте.
# Задачу необходимо решить с использованием словаря.

txt = input('\nВведите текст:\t')
print()
lst = txt.split()
dct = {}

for word in lst:
    val = dct.get(word, 0)
    dct[word] = val + 1

print('\t\'Слово\'  :  Кол-во появлений в тексте')
print('\t---------------------------------------')
print(dct)
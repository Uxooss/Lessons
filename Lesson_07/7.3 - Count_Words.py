# В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте.
# Задачу необходимо решить с использованием словаря.

i = 'Слово: \"{}\", встречается {} раз(а).'
lst = (input('\nВведите текст:\t')).split()
dct = {}

for word in lst:
    val = dct.get(word, 0)
    dct[word] = val + 1

for key, val in dct.items():
    print(i.format(key, val))

# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
# Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

n = int(input('\nВвеидте количество учеников:\t'))
k = int(input('Введите количество яблок:\t\t'))
i = '\nКаждому ученику достанется по {} яблок(а) и {} яблок(а) останется в корзине.\n'
a = (k // n)
b = (k % n)
print('-' * 74, (i.format(a, b)), '.' * 72)

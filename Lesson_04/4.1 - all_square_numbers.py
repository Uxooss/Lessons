# По данному целому числу n распечатайте все квадраты натуральных чисел,
# не превосходящие n, в порядке возрастания.

n = int(input('\nВведите целое, положительное число:\t'))
t = '\nКвадраты чисел, не превосходящие число {}\n - это числа:\t{}'

n = abs(n)
a = 0
s = 0
i = ''

while s < n:
    s = a + 1
    a += 1
    s *= a
    if s > n:
        continue
    i += str(s) + ' '
    
print(t.format(n, i))

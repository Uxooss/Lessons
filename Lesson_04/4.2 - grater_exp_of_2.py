# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
#
# Операцией возведения в степень, а так же функцией возведения в степень пользоваться НЕЛЬЗЯ!

n = int(input('\nВведите натуральное число:\t'))
i = '\nНаибольшая целая степень "двойки": {}\nПоказатель степени: {}'
ii = '\n\n\t\t2 ** {} = {}'

e = 2
c = 0

while e <= n:
    e *= 2
    c += 1
    if e > n:
        break
e = int(e / 2)

print(i.format(e, c), ii.format(c, e))

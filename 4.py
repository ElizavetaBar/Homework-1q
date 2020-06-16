n = int(input('Введите любое целое число: '))

while n <= 0:
    n = int(input('Введите положительное число: '))
    if n > 0:
        continue
m = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > m:
        m = n % 10
    if n > 9:
        continue
    else:
        print('Самая большая цифра в числе: ', m)
        break

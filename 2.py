a = int(input('Введите количество секнуд: '))

hour = a//3600
minutes = (a//60) % 60
seconds = a % 60

if hour < 10:
    hour = str('0' + str(hour))
else:
    str(hour)
if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    str(minutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    str(seconds)
print(f'{hour}.{minutes}.{seconds}')



q = int(input('Укажите кол-во билетов для покупки: '))

s = 0
for i in range(q):
    age = int(input('Возраст:'))
    if age < 18:
        s = s + 0
    elif 18 <= age < 25:
        s = s + 990
    else:
        s = s + 1390
if q > 3:
    f = 0.9
else:
    f = 1
print ('Общая стоимость: ', s*f, 'руб.')

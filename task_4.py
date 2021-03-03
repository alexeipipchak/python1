number = int(input('Введите целое положительное число: '))
b = 0
if number > 0:
    while number > 0:
        a = number % 10
        if b < a:
            b = a
        number = number // 10
    print("Самая большая цыфра в вашем числе: " + str(b))
else:
    print('Вы ввели отрицательное число!')

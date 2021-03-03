number = int(input("Введите число секунд: "))
hour = number // 3600
a = number % 3600
minute = a // 60
second = a % 60
print('%02d' % hour + ":" + '%02d' % minute + ":" + '%02d' % second)

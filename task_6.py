a = int(input('Сколько километров пробежал спортсмен в первый день: '))
b = int(input('Введите сколько километров надо пробежать спортсмену: '))
c = float(a)
i = 1
while c <= b:
    print(str(i) + ' день: ' + "%.2f" % c)
    i = i + 1
    c += c * 0.1
    if c > b:
        print(str(i) + ' день: ' + "%.2f" % c)
print("На " + str(i) + ' день, спортсмен пробежит ' + str(b) + ' километра.')
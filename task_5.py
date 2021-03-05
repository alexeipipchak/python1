revenue = int(input('Ведите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print('Прибыль фирмы - ' + str(profit))
    print('Рентабельность фирмы - ' + str(profitability))
    staff = int(input('Введите количество сотрудников фирмы: '))
    profit_staff = profit / staff
    print('Прибыль фирмы на одного сотрудника равна - ' + str(profit_staff))
else:
    print('Прибыли нету! ')
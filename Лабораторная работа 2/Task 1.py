money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
m=0
summa = money_capital
while True:
    summa = summa + salary - spend * (1+increase*m)
    if summa < 0:
        break
    else:
        m=m+1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", m-1)

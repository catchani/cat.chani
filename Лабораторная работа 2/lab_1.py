money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    balance = spend - salary
    if balance > money_capital:
        break

    count += 1
    money_capital -= balance
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", count)

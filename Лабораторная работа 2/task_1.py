money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
while True:
    deficit = spend - salary  # Дефицит в этом месяце
    money_capital -= deficit
    months += 1
    spend *= (1 + increase)  # Только траты растут на следующий месяц
    if money_capital < deficit:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
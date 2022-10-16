money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

#month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение


def how_much(capital, profit, lost, inflation):
    total = 0
    while capital >= lost * (1+inflation):
        capital += profit
        lost = lost * (1+inflation)
        capital -= lost
        total += 1
    return total


month = how_much(money_capital, salary, spend, increase)

print(month)

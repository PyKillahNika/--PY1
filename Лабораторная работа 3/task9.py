salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

# need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение


def how_much(profit, lost, inflation, time):
    total = 0
    total += profit
    total -= lost
    for i in range(time-1):
        lost = lost * (1 + inflation)
        total -= lost
        total += profit
    return total*-1


need_money = how_much(salary, spend, increase, months)

print(round(need_money))

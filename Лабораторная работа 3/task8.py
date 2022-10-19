money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# TODO Оформить решение
""" "Для чего здесь - lost * (1+inflation)?" (с) ksigorodetskaya - 
    предположим, что на старте капитал 5001, траты 5000, ЗП 0, а инфляция>0, 
    тогда получается через более простое условие мы пройдем в вайл и 
    увеличим количество месяцев, хотя по факту на этой итерации трата
     увеличится до >5001, что больше капитала """


def how_much(capital, profit, lost, inflation):
    total = 0
    while capital >= lost * (1+inflation):
        lost = lost * (1+inflation)
        capital += profit - lost
        total += 1
    return total


month = how_much(money_capital, salary, spend, increase)
print(month)

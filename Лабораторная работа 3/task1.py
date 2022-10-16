src = not False and True or False and not True

# TODO расписать упрощение выражения
#result = True and True or False and False #избавляемся от NOT
#result = True or False #избавляемся от AND
#result = True #избавляемся от OR
result = True  # TODO подставить результат выражения

print(src == result)

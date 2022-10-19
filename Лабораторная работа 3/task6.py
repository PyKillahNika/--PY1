list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
super_high = list_numbers[0]
# ищем максимальное через цикл (не используем max())
for each in list_numbers:
    super_high = each * int(each > super_high) + super_high * int(not each > super_high)
# реплейсим
list_numbers[len(list_numbers)-1], list_numbers[list_numbers.index(super_high)] =\
    list_numbers[list_numbers.index(super_high)], list_numbers[len(list_numbers)-1]
print(list_numbers)

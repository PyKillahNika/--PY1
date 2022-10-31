def get_count_char(str_):
    str_ = str_.lower()
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    slovar = dict()
    for each in range(len(str_)):
        if str_[each].isalpha():
            if str_[each] in slovar:
                slovar[str_[each]] += 1
            else:
                slovar[str_[each]] = 1
    return slovar


def percentil(dictionary):
    total = sum(dictionary.values())
    for each in dictionary:
        dictionary[each] = f'{dictionary[each]/total*100} %'
    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percentil(get_count_char(main_str)))

def delete(list_, index=None):
    if index is None or abs(index) > len(list_):
        list_ = list_[0:-1]
    elif index > -1:
        list_ = list_[0:index] + list_[index+1:len(list_)]
    else:
        list_ = list_[0:len(list_)+index] + list_[len(list_)+index+1:len(list_)]

    return list_
# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=1))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]

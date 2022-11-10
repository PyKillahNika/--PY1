from random import sample


def get_unique_list_numbers(len_: int = 15, min_: int = -10, max_: int = 10) -> list[int]:
    list_of_all_numbers_ = [each for each in range(min_, max_+1, 1)]
    list_ = sample(list_of_all_numbers_, len_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

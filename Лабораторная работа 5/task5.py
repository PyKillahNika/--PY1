from string import ascii_letters, digits
from random import sample


def get_random_password(len_: int = 8) -> str:
    str_ = "".join(sample(ascii_letters + digits, len_))
    return str_


print(get_random_password())

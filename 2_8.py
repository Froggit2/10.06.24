class Error_1(Exception):

    def __init__(self, SMS):
        self.SMS = SMS


class Error_2(Exception):
    def __init__(self, SMS):
        self.SMS = SMS


def F(x, y):
    a = x + y
    if a == 3.14:
        raise Error_1("Я не люблю число Пи")
    if x == 0 or y == 0:
        raise Error_2("Я не люблю ноль")
    return a


try:
    summa = F(0, 0)
    print(summa)
except Error_1 as E1:
    print(E1)
    raise Error_1('Нашёл число Пи!')
except Error_2 as E2:
    print(E2)
    raise Error_2('Нашёл ноль!')
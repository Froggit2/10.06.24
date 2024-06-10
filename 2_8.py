class Erorr_1(Exception):

    def __init__(self, SMS):
        self.SMS = SMS


class Error_2(Exception):
    def __init__(self, SMS):
        self.SMS = SMS


def F(x, y):
    a = x + y
    if a == 3.14:
        raise Erorr_1("Я не люблю число Пи")
    if a == 0:
        raise Error_2("Я не люблю ноль")
    return a


try:
    summa = F(3, 0.14)
    print(summa)
except Erorr_1 as E1:
    print(E1)
except Error_2 as E2:
    print(E2)
class BankError(Exception):
    pass


class ZeroFundError(BankError):
    pass


try:
    1 / 0
except (ValueError, ZeroDivisionError):
    print("Общая ошибка")

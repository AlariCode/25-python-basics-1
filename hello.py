class InvalidAgeError(Exception):
    pass


def set_age(age: int):
    if age < 0:
        raise InvalidAgeError("Возраст должен быть больше 0")
    return age


try:
    set_age(-1)
except InvalidAgeError as e:
    print(e)

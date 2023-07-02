def validate_int_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Все параметры должны быть целыми числами")
        return func(*args)

    return wrapper


@validate_int_parameters
def sum(a, b):
    return a + b


print(sum(5, "Hello"))

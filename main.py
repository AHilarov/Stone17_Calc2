string = input('Введите пример: ')
string = string.replace(' ', '')

operation = {'*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '+': lambda x, y: x + y,
             '-': lambda x, y: x - y}


def str_to_list(instance: str) -> list | None:
    instance = instance.replace(' ', '')
    instance = instance.replace('+', ' + ').replace('*', ' * '). \
        replace('/', ' / ').replace('-', ' + -').split()
    for i in range(len(instance)):
        try:
            instance[i] = int(instance[i])
        except:
            pass
    if isinstance(instance[0], str):
        instance.pop(0)
    i = 0
    while i < (len(instance) - 1):
        if isinstance(instance[i], str) and instance[i + 1] == '+':
            instance.pop(i + 1)
        else:
            i += 1
    if validate(instance):
        return instance
    else:
        return None


def validate(instance: list) -> bool:
    if len(instance) % 2 == 0:
        return False
    for i in range(0, len(instance), 2):
        if not isinstance(instance[i], int):
            return False
    return True


def calculate(instance: list) -> str:
    if instance:
        while len(instance) > 1:
            while '*' in instance or '/' in instance:
                double_calculate(instance, '*', '/')
            while '+' in instance or '-' in instance:
                double_calculate(instance, '+', '-')
        return instance[0]
    else:
        return 'Введено неверное выражение'


def simple_calculate(instance: list, i: int, sign: str):
    instance[i - 1] = operation.get(sign)(instance[i - 1], instance[i + 1])
    instance.pop(i)
    instance.pop(i)


def double_calculate(instance: list, sign_1: str, sign_2: str):
    i = 0
    while i < (len(instance) - 1):
        if instance[i] == sign_1:
            simple_calculate(instance, i, sign_1)
        elif instance[i] == sign_2:
            simple_calculate(instance, i, sign_2)
        else:
            i += 1
    return instance


print(calculate(str_to_list(string)))
print(eval(string))

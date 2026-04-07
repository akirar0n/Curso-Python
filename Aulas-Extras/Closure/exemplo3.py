################################################################################


#
# Exemplos de closures
#
from collections.abc import Callable
from typing import Protocol


# Factory (fábrica de funções)
def make_multiplier(multiplier: float, /) -> Callable[[float], float]:
    def multiplier_times(multiplicand: float, /) -> float:
        return multiplicand * multiplier

    return multiplier_times


# print("\nMultiplicadores")
# times_two = make_multiplier(2)  # Função interna precisará lembrar do 2
# times_three = make_multiplier(3)  # Nesse caso do 3

# print("3 * 2 =   ", times_two(54))  # 3 * [2] = 6 - [2] lembrado
# print("3 * 5 =   ", times_three(5))  # 5 * [3] = 15 - [3] lembrado

################################################################################


# Validador simples
def make_lt_checker(min_value: int) -> Callable[[int], bool]:
    def is_lt(value: int) -> bool:
        return value < min_value

    return is_lt


# print("\nValidatores simples")
# lt_ten = make_lt_checker(10)  # 10 precisa ser lembrado

# print("30 < 10   ", lt_ten(30))  # 30 é menor do que 10? False
# print("9 < 10   ", lt_ten(9))  # 9 é menor do que 10? True

################################################################################

def with_callback(value: str, callback: Callable[[str], str]) -> Callable[[], str]:
    # Você também poderia realizar algo aqui
    def runner() -> str:
        print(f"Realizando alguma operação com o valor {value!r}")
        return callback(value)

    return runner


def my_callback(value: str) -> str:
    print(f"Valor {value!r} recebido no callback")
    return value + " (callback executed)"


# print("\nCallback")

# execute_operation = with_callback("## Exemplo ##", callback=my_callback)
# result = execute_operation()
# print(f"Callback:    {result!r}")


################################################################################

class Operation[**P, R](Protocol):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...


def cacher[**P, R](callback: Operation[P, R]) -> Callable[P, R]:
    cached_params: dict[tuple[object, ...], R] = {}

    def closure(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in cached_params:
            result = cached_params[args]
            print(f"Cacher found result {result!r}")
        else:
            result = callback(*args, **kwargs)
        cached_params[args] = result

        return result

    return closure


def operation(*args: str) -> list[str]:
    import time

    values: list[str] = []

    for arg in args:
        print(f"Fazendo algo complexo ou demorado com {arg!r}...")
        time.sleep(1)
        values.append(arg)

    return values


# print("\nCacher")
# operation_cached = cacher(operation)

# op1 = operation_cached("a", "b", "c")
# op2 = operation_cached("a", "b", "c")  # em cache

# op4 = operation_cached("b", "b", "c")
# op5 = operation_cached("b", "b", "c")  # em cache

################################################################################

@cacher
def get_from_db(id: int, /) -> str:
    import time

    names = ["Luiz", "Maria", "Helena", "Letícia"]

    print(f"Returning value for ID {id}")
    time.sleep(2)
    return names[id]


print("\nCacher Decorator")

print(get_from_db(1))
print(get_from_db(1))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))
print(get_from_db(0))
print(get_from_db(2))
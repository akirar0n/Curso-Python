# ** Introspecção de closures
#

from collections.abc import Callable


def enclosing(a: str) -> Callable[[str], str]:
    def closure(b: str) -> str:
        return f"{a} {b}"

    return closure


same_closure = enclosing("João")  # aqui está o closure
this_is_result_str = same_closure("Otávio")  # isso é uma str

print()
print("enclosing")
# Como ver dados da função externa
# Variáveis exclusivamente locais
print("Varnames [Local    ]  ", enclosing.__code__.co_varnames)
# Variáveis do enclosing usadas nessa função
print("Freevars [Enclosing]  ", enclosing.__code__.co_freevars)
# Variáveis dessa função usadas em funções internas
print("Cellvars [Usadas   ]  ", enclosing.__code__.co_cellvars)
# Células da closure se existir
print("Closure  [Closure  ]  ", enclosing.__closure__)

print()
print()
print("same_closure")
# Como ver dados da função interna
# Variáveis exclusivamente locais
print("Varnames [Local    ]  ", same_closure.__code__.co_varnames)
# Variáveis do enclosing usadas nessa função
print("Freevars [Enclosing]  ", same_closure.__code__.co_freevars)
# Variáveis dessa função usadas em funções internas
print("Cellvars [Usadas   ]  ", same_closure.__code__.co_cellvars)
# Células da closure se existir
print("Closure  [Closure  ]  ", same_closure.__closure__[0].cell_contents)


################################################################################
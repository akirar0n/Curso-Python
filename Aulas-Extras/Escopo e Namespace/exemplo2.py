""" Módulo exemplo 1"""
""" 

------------- Escopo -------------

É a região do código onde um nome está diretamente acessível.
Ele determina as limites e o tempo de vida dos nomes definidos internamente.

É usado para encapsular o código e evitar colisões de nome e efeitos colaterais indesejados.

Tipos de escopos: Built-In, Global, Enclosing e Local.
São escopos dinâmicos

Cada escopo tem seu "espaço de nome" (namespace)
----------------------------------

"""

# nome definido no escopo global (módulo)
um_nome = 'um_nome (GLOBAL)'

def func_global(sou_local: str) -> None:
    # Escopo local 
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"

    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")

print("Nome do módulo:", __name__)
print("Arquivo do módulo:", __file__)
print("Documentação do módulo:", __doc__)
print()

func_global("arg (local)")

print(f"Fora da função: {um_nome}")
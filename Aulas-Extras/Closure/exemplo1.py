#
# Closures em Python
#
# O que são closures?
# Closures ocorrem quando funções internas, definidas dentro de outras funções,
# referenciam variáveis livres do seu escopo. Variáveis livres são as
# variáveis que não foram definidas no escopo da função interna (são da função
# externa).
# Se a função externa retornar apenas a referência da função interna, então
# o interpretador precisará atrelar quaisquer referências a variáveis livres
# que a função interna precisar para que ela possa ser executada corretamente.
# São muito usados em programação funcional, decoradores de função e algoritmos
# em geral.

def externa(a):
    #Enclosing
    def interna(b):
        #função interna precisa de 'a'
        return f"{a} {b}"

    return interna

incompleto = externa("Roney")   
completo = incompleto("Vila")

print(completo)
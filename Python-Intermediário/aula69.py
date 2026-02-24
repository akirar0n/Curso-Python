# Higher Order Functions

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# v = executa()
print(
    executa(saudacao, 'Bom dia', 'Roney')
)

print(
    executa(saudacao, 'Boa noite', 'Jorge')
)
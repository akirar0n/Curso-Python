# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = { 
    'nome': 'Roney',
    'sobrenome': 'Vila Nova dos Santos',
    'idade': 20,
    'altura': 1.83,
    'endereços': [
        {'rua': 'tal tal', 'número': 123}
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

pessoa2 = {}

# 
# 

chave2 = 'nome'

pessoa2[chave2] = 'Roney'
pessoa2['sobrenome'] = 'Vila'

print(pessoa2[chave2])

pessoa2[chave2] = 'Ana'

del pessoa2['sobrenome']
print(pessoa2)
print(pessoa2['nome'])

if pessoa2.get('sobrenome') is None:
    print('Existe')
else: 
    print(pessoa2['sobrenome'])
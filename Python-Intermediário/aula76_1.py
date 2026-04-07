from re import S
from tkinter import N


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
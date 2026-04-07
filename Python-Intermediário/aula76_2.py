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
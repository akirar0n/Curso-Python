lista = ['Maria', 'Roney', 'José']
lista.append('Jorge')
indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena', ],
    # 0
    ['Elaine', ],
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],
]
# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep ='\n')
# Iterável -> str, range, etc
# Iterador -> quem saber entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

# texto = iter('Roney') # __iter__()

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

texto = 'Roney' # iterável
# iterador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except: 
#         break

for letra in texto:
    print(letra)
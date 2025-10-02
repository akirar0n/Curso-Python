primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor == segundo_valor: 
    print('Valores iguais')
elif primeiro_valor > segundo_valor:
    print('Primeiro valor', '(', primeiro_valor, ')', 'é maior que o segundo','(', segundo_valor, ')')
elif primeiro_valor < segundo_valor:
    print('Segundo valor', '(', segundo_valor, ')', 'é maior que o primeiro','(', primeiro_valor, ')')

# if primeiro_valor > segundo_valor:
#     print(
#         f'{primeiro_valor=} é maior ou igual '
#         f'ao que {segundo_valor}'
#     )
# else:
#     print(
#         f'{segundo_valor=} é maior ou igual'
#         f'ao que {primeiro_valor}'
#     )
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

numero_str = input(
    'Vou dobrar o número digitado: '
)

try: 
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('Isso não é um número')
# numero_float = float(numero)
# print(f'O dobro de {numero} é {numero_float * 2:.0f}')
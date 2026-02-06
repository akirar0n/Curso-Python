# Exercício 1 

try:
    numero_str = input('Digite um número inteiro: ')
    numero = int(numero_str)

    if numero % 2 == 0:
        print(f'Número {numero} é par')
    else:
        print(f'Número {numero} é impar')
except:
        print('Erro: Este numero não é inteiro!')

# Exercício 2

entrada = input('Qual a hora da sua região: ')

try:
    horario = int(entrada)

    if horario >= 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('Não reconheço este horário')
except:
    print('Por favor, digite apenas um número válido')

# Exercício 3

nome = input('Insira seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande')
else: 
    print('Por favor, digite algo!')
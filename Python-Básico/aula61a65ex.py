"""
--------CÁLCULO DO PRIMEIRO DÍGITO--------

CPF: 746.824.890-70
Soma dos 9 primeiros dígitos multiplicando 
cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746824890

10  9  8  7  6  5  4  3 2
*7  4  6  8  2  4  8  9 0
--------------------------
70 36 48 56 12 20 32 27 0

Somar todos resultados:
70+36+48+56+12+20+32+27+0 = 301
301 * 10 = 3010
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é valor da conta

O primeiro dígito do CPF é 7    
""" 

"""
--------CÁLCULO DO SEGUNDO DÍGITO--------

CPF: 746.824.890-70
Soma dos 9 primeiros dígitos, mais o PRIMEIRO dígito
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 7468248907

    11 10  9  8  7  6  5  4  3  2
*    7  4  6  8  2  4  8  9  0  7
    ------------------------------
    77 40 54 64 14 24 40 36  0 14

Somar todos resultados:
77+40+54+64+14+24+40+36+0+14 = 363
363 * 10 = 3630
3630 % 11 = 0

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é valor da conta

O primeiro dígito do CPF é 0
"""
import random
for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11 
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_calculo )
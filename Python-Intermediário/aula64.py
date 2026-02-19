def soma(x, y, z=0):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else: 
        print(f'{x=} {y=}', x + y)

def divisao(a, b):
    print(a / b)

def multiplicacao(c, d):
    print(c * d)

def subtracao(e, f):
    print(e - f)

soma(1, 2)
soma(10, 20, 0)
divisao(0, 50)
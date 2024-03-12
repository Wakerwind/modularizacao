def metade(p,f = False):

    if f:
        return format(p / 2)
    else:
        return p / 2

def dobro(p, f = False):

    if f == True:
        return format(p * 2)
    else:
        return p*2

def aumento(p,percent, f = False):
    if f:
        return format(p + p * (percent / 100))
    else:
        return p + p * (percent / 100)

def reduc(p,percent, f = False):
    if f == True:
        return format(p - p * (percent / 100))
    else:
        return p - p * (percent / 100)

def format(p):
    return f'R${p:.2f}'.replace('.', ',')

def resumo(p, inc, dec):

    print('-'*30)
    print(f'{"RESUMO DO VALOR":^15}')
    print('-'* 30)

    print(f'Preço analisado: {p:>10}')
    print(f'Dobro do preço: {dobro(p):>10}')
    print(f'Metade do preço: {metade(p):>10}')
    print(f'80% de aumento: {aumento(p,inc):>10}')
    print(f'35% de redução: {reduc(p,dec):>10}')

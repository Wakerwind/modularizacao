from modulos import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% fica {moeda.aumento(p,10)}')
print(f'Reduzindo em 13% fica {moeda.reduc(p,13)}')

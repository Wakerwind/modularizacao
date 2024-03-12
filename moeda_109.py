from modulos import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.format(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.format(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% fica {moeda.aumento(p,10,True)}')
print(f'Reduzindo em 13% fica {moeda.reduc(p,13,True)}')
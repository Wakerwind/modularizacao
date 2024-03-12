from modulos import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.format(p)} é {moeda.format(moeda.metade(p))}')
print(f'O dobro de {moeda.format(p)} é {moeda.format(moeda.dobro(p))}')
print(f'Aumentando em 10% fica {moeda.format(moeda.aumento(p,10))}')
print(f'Reduzindo em 13% fica {moeda.format(moeda.reduc(p,13))}')


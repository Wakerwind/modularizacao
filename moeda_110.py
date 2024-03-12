from modulos import moeda
from modulos import dado

p = float(dado.leiaDinheiro('Digite o preço: R$ '))

moeda.resumo(p,80,35)
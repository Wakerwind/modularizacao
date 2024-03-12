def leiaDinheiro(msg):

   while True:

       p = input(msg).replace(',', '.').strip()

       if p.isalpha() or p == '':
           print(f'ERRO: {p} é um preço inválido!')

       else:
           return p
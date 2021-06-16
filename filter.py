pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}

]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

maiores = filter(lambda p: p['idade'] >= 18, pessoas)
print(list(maiores))

nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nomes_grandes))

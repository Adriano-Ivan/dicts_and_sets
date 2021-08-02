from collections import defaultdict
from collections import Counter

class Conta:
    def __init__(self):
        print('Imprimindo mensagem de construção...')

texto = 'O cachorro é vermelho, e o vermelho é a cor da paixão. O cachorro é apaixonado pelo vermelho.'
texto = texto.split()

set_texto = set(texto)
print(set_texto)

aparicoes = {'cachorro': 2, 'vermelho': 3, 'é': 3, 'o': 4}

print(aparicoes['cachorro'])
print(aparicoes['vermelho'])
print(aparicoes['é'])
print(aparicoes['o'])

print(aparicoes.get('dfd', 0))

# aparicoes2 = dict(Espada = 3, Chines = 5)
# print(aparicoes2)

aparicoes['córrego'] = 3
aparicoes['córrego'] = 15

print(aparicoes)

del(aparicoes['é'])

print(aparicoes)

print('rio' in aparicoes)
print('córrego' in aparicoes)

print()
for elemento in aparicoes:
    print(elemento)

print()
for elemento in aparicoes.keys():
    print(elemento)

print()
for elemento in aparicoes.values():
    print(elemento)

print()
for chave, valor in aparicoes.items():
    print(f'{chave} -> {valor}')

print()
print(3 in aparicoes.values())

lista_palavras_em_dicionario = ['palavra {}'.format(palavra) for palavra in aparicoes.keys()]
print(lista_palavras_em_dicionario)

# del(aparicoes['córrego'])
# print(aparicoes)

texto = 'O céu é negro, assim como o cobertor noturno é negro, noturno é o planeta negro'
texto = texto.lower()
texto = texto.split()

aparicoes = Counter()

for palavra in texto:
    aparicoes[palavra] += aparicoes[palavra] + 1


print(aparicoes)

contas = defaultdict(Conta)

aparicoes2 = Counter(texto)
print(aparicoes2)
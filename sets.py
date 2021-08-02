
usuarios_data_science = [23, 24, 87, 21]
usuarios_machine_learning = [13, 24, 32, 42]

assistiram = []
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(len(assistiram))

assistiram = set(assistiram)
print(assistiram)
print(type(assistiram))

for e in assistiram:
    print(e)

print()
usuarios_data_science = {23, 24, 87, 21}
usuarios_machine_learning = {13, 24, 32, 21}

uniao = usuarios_machine_learning | usuarios_data_science
print(uniao)

intersection = usuarios_machine_learning & usuarios_data_science
print(intersection)

subtracao = usuarios_data_science - usuarios_machine_learning
print(subtracao)
print(23 in subtracao)
print(24 in subtracao)

exclusivos = usuarios_data_science ^ usuarios_machine_learning
print(exclusivos)

print()
usuarios = {1, 87, 23, 32, 76, 98, 12, 16, 17}
usuarios.add(123)
print(len(usuarios))
print(usuarios)

usuarios_imutavel = frozenset(usuarios)
print(usuarios_imutavel)

print(type(usuarios))
print(type(usuarios_imutavel))

texto = 'Bem-vindo, meu nome é Adriano, tenho 19 anos, e gosto do meu nome . Estou estudando programação, e programação é muito interessante.'
texto = texto.split()
print(texto)
texto_set = set(texto)
print(texto_set)
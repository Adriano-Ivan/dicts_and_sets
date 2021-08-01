
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
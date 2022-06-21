discoDado = [5000,7000,9000,11000,13000]

undo =  [('t3', 3, 'salario', 9000, 45454), ('t5', 5, 'salario', 13000, 45455)]
x = [s for s in undo]

print("undo:",undo)
print("dados:",discoDado)

for i in undo:
    print("ID:",i[:][1])
    posicao = i[:][1]
    print("disco:",discoDado[posicao-1])
    discoDado[posicao-1] = i[:][4]

print(discoDado)

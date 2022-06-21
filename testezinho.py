redo = [('t1', 1, 'salario', 5000, 1515), ('t2', 2, 'salario', 7000, 151626), ('t4', 4, 'salario', 11000, 845454)] 
undo = [('t3', 3, 'salario', 9000, 5494984), ('t5', 5, 'salario', 13000, 9885484)]

discoDado = [1111, 2222, 3333, 4444, 13000]

def falha():
    for i in undo:
        #print("ID:",i[:][1])
        posicao = i[:][1]
        #print("disco:",discoDado[posicao-1])
        val = int(i[:][3])
        discoDado[posicao-1] = val
        #print("Teste apos falha:", discoDado)
    """
    for i in undo:
        print("ID:",i[:][1])
        posicao = i[:][1]
        print("disco:",discoDado[posicao-1])
        discoDado[posicao-1] = i[:][4]
        """
print("undo:",undo,"\n")
print("pre falha Dados:",discoDado,"\n")

falha()
print("pos falha Dados:",discoDado)

redo = []
memoriaLog = [('t1', 1, 'salario', 5000, 22222), ('t2', 3, 'salario', 9000, 3333)]
undo = []


t = str(input("Transacao: "))
redo.append([s for s in memoriaLog if t in s])

for s in redo:
    if s not in memoriaLog:
        undo.append(s)
        break
    else:
        break
        #print("===",s)


print(redo)
print(memoriaLog)
print(undo)
redo = []
memoriaLog = [('t1', 1, 'salario', 5000, 22222), ('t2', 3, 'salario', 9000, 3333), ('t3', 5, 'salario', 12000, 9)]
undo = []


t = str(input("Transacao: "))
redo = ([s for s in memoriaLog if t in s])


for s in memoriaLog:
    if s not in redo:
        undo.append(s)
        
             
        
    

      


print("redo:",redo)
print("memoria:",memoriaLog)
print("undo:",undo)
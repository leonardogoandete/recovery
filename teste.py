
memoriaLog = [('t1', 1, 'salario', 5000, 22222), ('t2', 3, 'salario', 9000, 3333), ('t3', 5, 'salario', 12000, 9)]


#print(memoriaLog.split(','))

f = open("teste.txt", "a")

for memoriaLog in memoriaLog:
    print(memoriaLog)
    f.write(str(memoriaLog)+"\n")
f.write(str("<CHECKPOINT>\n"))
f.close
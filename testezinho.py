discoDado = [5000,7000,9000,11000,13000]

undo =  [('t3', 3, 'salario', 9000, 45454), ('t5', 5, 'salario', 13000, 45455)]

x = [s for s in undo]

k = 0

for i in x:
    #if i[:][4]:
        if i[:][1] == len(discoDado):
            #print(i)
            print("ID:",i[:][1])
            print("==",i[:][4])
            before = i[:][3]
            print(before)
            print("dd:",discoDado[k])
        else:
            k+=1

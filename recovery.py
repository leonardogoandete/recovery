import os
discoLog = []
memoriaLog = []
memoriaDado = [5000,7000,9000,11000,13000]
discoDado = [5000,7000,9000,11000,13000] 
redo = [] # 
undo = []

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def commit():
    try:
        t = input("Digite a transação:")
        discoLog[:] += ([s for s in memoriaLog if t in s])
        redo[:] += ([s for s in memoriaLog if t in s]) #
        # REDO joga pro disco
        print("Transação",t,"commitada com sucesso!")     
    except:
        print("== Erro ao realizar commit!")
    
def checkpoint():
    #try:
        #discoDado[:] = memoriaDado[:]
        if(os.path.exists('discodado.txt')):
            f = open("discodado.txt", "w")
            #f.write(str(discoDado)+"\n")
            f.write(str(memoriaDado[:])+"\n")
            f.close
        else:
            print("O arquivo \"discodado.txt\" nao existe!")
        ##########
        if(os.path.exists('discolog.txt')):
            #discoLog[:] = memoriaLog[:]
            f = open("discolog.txt", "a")
            #f.write(str(discoLog)+"\n")
            for i in memoriaLog:
                f.write(str(i)+"\n")
            f.write(str("<CHECKPOINT>\n"))
            f.close
        else:
            print("O arquivo \"discolog.txt\" nao existe!")
        #discoLog.append("<CHECKPOINT>")
        redo[:] = memoriaLog[:] # professorra pode dar checkpoint antes do commit e vice versa
    #except:
    #    print("Erro ao realizar Checkpoint")
def fUndo():
    #redo
    #auxCommit ou discoLog
    #undo.append([element for element in memoriaLog if element not in redo])
    undo[:] += ([s for s in memoriaLog if s not in redo])  

def falha():
    fUndo()
    memoriaLog.clear() 
    memoriaDado.clear()     

def update():
    try:
        numTransacao = input("Digite a transacao: ")
        idValor = int(input("ID da pessoa: "))
        velhoVal = discoDado[idValor - 1]
        novoVal = int(input("Digite o valor: "))
        memoriaLog[:] += [(numTransacao,idValor,"salario",velhoVal,novoVal)]
        memoriaDado[idValor - 1] = novoVal
        print("Sucesso ao fazer Update!")
    except:
        limpaTela()
        print("== Erro ao fazer update!")
#Transação | ID da pessoa | atributo | valor Antigo | Valor novo
def menu():
    print("a - Visualizar Log na memoria")
    print("b - Visualizar Log no disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("g - Visualizar dados no disco")
    print("h - Visualizar dados na memoria")
    print("i - Visualizar UNDO e REDO")
    print("s - Sair do programa")
    print("Digite a opcao: ")

i = None
while i != 's':
    menu()
    i = input().lower()
    if i == 'a':
        print(memoriaLog)
    elif i == 'b':
        f = open("discolog.txt", "r")
        print(f.read())
        f.close
    elif i == 'c':
        update()
    elif i == 'd':
        checkpoint()
    elif i == 'e':
        #chamar Undo e Redo
        falha()
    elif i == 'f':
        commit()
    elif i == 'g':
        f = open("discodado.txt", "r")
        print(f.read())
        f.close
        #print(discoDado)
    elif i == 'h':
        print(memoriaDado)
    elif i == 'i':
        print("REDO",redo,"\nUNDO",undo)
    else:
        print("Saindo...")
        break
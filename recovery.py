import os
discoLog = []
memoriaLog = []
memoriaDado = [5000,7000,9000,11000,13000]
discoDado = [5000,7000,9000,11000,13000] 
redo = []
undo = []
memoriaTest = [] 
dadosDisco = 'discodado.txt'
logsDisco = 'discolog.txt'

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def commit():
    try:
        t = input("Digite a transação:")
        discoLog[:] += ([s for s in memoriaLog if t in s])
        redo[:] += ([s for s in memoriaLog if t in s]) #
        if(os.path.exists(logsDisco)):
            f = open(logsDisco, "w")
            for i in discoLog:
                f.write(str(i)+"\n")
            f.close
            print("Transação",t,"comitada com sucesso!")
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
    except:
        print("== Erro ao realizar commit!")
    
def checkpoint():
    try:
        if(os.path.exists(dadosDisco)):
            with open(dadosDisco,'w') as f:
                f.write(str(memoriaDado[:])+"\n")
            memoriaTest[:] += memoriaDado[:]
        else:
            print("O arquivo \"DadosDisco.txt\" nao existe!")
        if(os.path.exists(logsDisco)):
            with open(logsDisco, 'w') as f:
                for i in memoriaLog:
                    f.write(str(i)+"\n")
                f.write(str("<CHECKPOINT>\n"))
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
    except:
        print("Erro ao realizar Checkpoint")    

def falha():
    #chamar Undo e Redo
    undo[:] += ([s for s in memoriaLog if s not in redo])
    for i in undo:
        posicao = i[:][1]
        val = int(i[:][3])
        discoDado[posicao-1] = val
        memoriaTest[posicao-1] = val
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
    print("MEMORIA:",memoriaDado)
    print("Tx MEMORIA:",memoriaLog,"\n")
    print("a - Visualizar Log da memoria")
    print("b - Visualizar Log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("g - Visualizar dados no disco")
    print("h - Visualizar dados na memoria")
    print("i - Visualizar dados UNDO e REDO")
    print("s - Sair do programa")
    print("Digite a opcao: ")

i = None
while i != 's':
    menu()
    i = input().lower()
    if i == 'a':
        print(memoriaLog)
    elif i == 'b':
        if(os.path.exists(logsDisco)):
            with open(logsDisco, 'r') as f:
                print(f.read())
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
    elif i == 'c':
        update()
    elif i == 'd':
        checkpoint()
    elif i == 'e':
        falha()
    elif i == 'f':
        commit()
    elif i == 'g':
        if(os.path.exists(dadosDisco)):
            with open(dadosDisco, 'r') as f:
                print(f.read())
        else:
            print("O arquivo \"DadosDisco.txt\" nao existe!")
    elif i == 'h':
        print(memoriaDado)
    elif i == 'i':
        print("REDO",redo,\
            "\nUNDO",undo)
    else:
        print("Saindo...")
        break
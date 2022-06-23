import os
discoLog = []
memoriaLog = []
memoriaDado = [5000,7000,9000,11000,13000]
discoDado = [5000,7000,9000,11000,13000] 
discoDadoAux = []
redo = []
undo = [] 
dadosDisco = 'discodado.txt'
logsDisco = 'discolog.txt'

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criaArquivos():
    if not (os.path.exists(logsDisco)):
        with open(logsDisco, 'w+') as f:
            f.close()
    if not (os.path.exists(dadosDisco)):
        with open(dadosDisco, 'w+') as f:
            f.close()
             
def commit():
    try:
        t = input("Digite a transação:")
        discoLog.extend([s for s in memoriaLog if t in s])
        redo.extend([s for s in memoriaLog if t in s]) #
        if(os.path.exists(logsDisco)):
            with open(logsDisco, 'w') as f:
                for i in discoLog:
                    f.write(str(i)+"\n")
            print("Transação",t,"comitada com sucesso!")
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
    except:
        print("== Erro ao realizar commit!")
    
def checkpoint():
    try:
        if(os.path.exists(dadosDisco)):
            with open(dadosDisco,'w') as f:
                f.write(str(memoriaDado)+"\n")
        else:
            print("O arquivo \"DadosDisco.txt\" nao existe!")
        if(os.path.exists(logsDisco)):
            with open(logsDisco, 'w') as f:
                for i in memoriaLog:
                    f.write(str(i)+"\n")
                f.write(str("<CHECKPOINT>\n"))
        else:
            print("O arquivo \"logDisco.txt\" nao existe!")
        print("Checkpoint realizado com sucesso!")
    except:
        print("Erro ao realizar Checkpoint!")    

def falha():
    undo.extend([s for s in memoriaLog if s not in redo])
    discoDadoAux = list(memoriaDado[:])
    for i in range(len(undo)):
        beforeImage = undo[i][3]
        # pega o CODIGO da pessoa e guarda na variavel ID
        id = undo[i][1]
        discoDadoAux[id-1] = beforeImage
    memoriaLog.clear() 
    memoriaDado.clear()
    with open('discodado.txt','w')as f:
            f.write(str(discoDadoAux))

def update():
    try:
        numTransacao = input("Digite a transacao: ")
        idValor = int(input("ID da pessoa: "))
        velhoVal = discoDado[idValor - 1]
        novoVal = int(input("Digite o valor: "))
        memoriaLog.append([numTransacao,idValor,"salario",velhoVal,novoVal])
        memoriaDado[idValor - 1] = novoVal
        print("Sucesso ao fazer Update!")
    except:
        limpaTela()
        print("== Erro ao fazer update!")

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
criaArquivos()
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
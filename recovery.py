discoLog = []
memoriaLog = []
memoriaDado = [5000,7000,9000,11000,13000]
discoDado = [5000,7000,9000,11000,13000] 
#transacao = [] # teste

def commit():
    try:
        y = 0
        t = input("Digite a transação:")
        for x in memoriaLog:
            if t in x:
                y=+1
            break
        discoLog.append(memoriaLog[y])
    except:
        print("== Erro ao realizar commit!")

def checkpoint():
    try:
        discoLog = memoriaLog
        discoDado = memoriaDado
        print("Sucesso ao fazer Checkpoint!")
    except:
        print("== Erro ao fazer checkpoint!")

def falha():
    memoriaLog.clear() 
    memoriaDado.clear()

def visualizaDiscoDados():
    print(discoDado)

def visualizaMemoriaDados():
    print(memoriaDado)

def update():
    try:
        numTransacao = input("Digite a transacao: ")
        idValor = int(input("ID da pessoa: "))
        velhoVal = discoDado[idValor - 1]
        novoVal = int(input("Digite o valor: "))
        memoriaLog.append((numTransacao,idValor,"salario",velhoVal,novoVal))
        memoriaDado[idValor - 1] = novoVal
        print("Sucesso ao fazer Update!")
    except:
        print("== Erro ao fazer update!")
#Transação | ID da pessoa | atributo | valor Antigo | Valor novo
def menu():
    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("g - Visualizar dados no disco")
    print("h - Visualizar dados na memoria")
    print("s - Sair do programa")
    print("Digite a opcao: ")

i = None
while i != 's':
    menu()
    i = input().lower()
    if i == 'a':
        print(memoriaLog)
    elif i == 'b':
        print(discoLog)
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
        visualizaDiscoDados()
    elif i == 'h':
        visualizaMemoriaDados()
    else:
        print("Saindo...")
        break
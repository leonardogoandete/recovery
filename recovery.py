logDisco = []
memoriaLog = []
memoriaDado = []
discoDado = [5000,7000,9000,11000,13000] 
#transacao = [] # teste

def commit():
    y = 0
    t = input("Digite a transação:")
    for x in memoriaLog:
      if t in x:
        y=+1
        break
    logDisco.append(memoriaLog[y])

def checkpoint():
    logDisco = memoriaLog
    #print(disco)

def falha():
    memoriaLog.clear() 
    memoriaDado.clear()

def update():
    numTransacao = input("Digite a transacao: ")
    idValor = int(input("ID da pessoa: "))
    velhoVal = discoDado[idValor - 1]
    novoVal = int(input("Digite o valor: "))
    memoriaLog.append((numTransacao,idValor,"salario",velhoVal,novoVal))
    memoriaDado.append((idValor,novoVal))
#Transação | ID da pessoa | atributo | valor Antigo | Valor novo
def menu():
    print("a - Visualizar buffer do Log")
    print("b - Visualizar log do disco")
    print("c - Update")
    print("d - Checkpoint")
    print("e - Falha")
    print("f - Commit")
    print("s - Sair do programa")
    print("Digite a opcao: ")

i = None
while i != 's':
    menu()
    i = input()
    if i == 'a':
        print(memoriaLog)
    elif i == 'b':
        print(logDisco)
    elif i == 'c':
        update()
    elif i == 'd':
        checkpoint()
    elif i == 'e':
        #chamar Undo e Redo
        falha()
    elif i == 'f':
        commit()
    else:
        print("Saindo...")
        break
    
    











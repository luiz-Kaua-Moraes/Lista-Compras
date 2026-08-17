listaCompra = []
entradaMenu = 0
adicionarItem = ""

removerItem = 0

def Menu():
    global entradaMenu

    print("-"*4)
    print("MENU")
    print("_"*4)

    print("1-Adicionar item à lista")
    print("2-Excluir item da lista")
    print("3-Mostrar lista")
    print("4-Sair")

    entradaMenu = int(input("Informe um número correspondente ao que deseja fazer:"))

def adicionar_item():
    global adicionarItem, sequenciaItem
    sequenciaItem = 0

    while True:
        sequenciaItem += 1
        adicionarItem = str(input(f"(Digite s quando quiser sair).{sequenciaItem}° item:")).capitalize()

            #Encerra a adição de itens  
        if adicionarItem == "S":
            break

        else:
            listaCompra.append(adicionarItem)

def remover_item():
    global removerItem

    mostrar_lista()
    while True:
        
        removerItem = int(input(f"(Digite s quando quiser sair).Digite o número correspondente ao item que deseja remover:"))

        #Ao digitar "s" o programa se encerra
        if adicionarItem == "S":
            break
        #falta fazer o básico(remover)
        else:
            listaCompra.remove()

def mostrar_lista():
    global sequenciaItem
    sequenciaItem = 0

    for item in listaCompra:
        sequenciaItem += 1
        print(f"{sequenciaItem}-{item}")
     
while True:
    Menu()
    match entradaMenu:
        case 1:
            adicionar_item()
        case 2:
            remover_item()
        case 3:
            mostrar_lista()
        case 4:
            break


listaCompra = []
entradaMenu = 0
adicionarItem = ""

numero = 0

def Menu():
    global entradaMenu

    print("\n-"*4)
    print("MENU")
    print("_"*4)

    print("1-Adicionar item à lista")
    print("2-Excluir item da lista")
    print("3-Mostrar lista")
    print("4-Sair")

    entradaMenu = int(input("\nInforme um número correspondente ao que deseja fazer:"))

def adicionar_item():
    global sequenciaItem
    sequenciaItem = 0

    print("\n-"*16)
    print("ADIÇÃO DOS ITENS")
    print("-*16")

    while True:
        sequenciaItem += 1
        adicionarItem = str(input(f"(\nDigite -1 quando quiser sair).{sequenciaItem}° item:")).capitalize()

            #Encerra a adição de itens  
        if adicionarItem == "-1":
            break

        else:
            listaCompra.append(f"{sequenciaItem}-{adicionarItem}")

def remover_item():

    mostrar_lista()

    print("-"*17)
    print("REMOÇÃO DOS ITENS")
    print("-"*17)
    while True:
        
        removerItem = int(input(f"(\nDigite -1 quando quiser sair).Digite o número correspondente ao item que deseja remover:"))
        numero = listaCompra[removerItem]

        #Ao digitar "-1" o programa se encerra
        if removerItem == -1:
            break
        #falta fazer o básico(remover)
        else:
            listaCompra.remove(numero)

def mostrar_lista():

    print("-"*16)
    print("LISTA DE COMPRAS")
    print("-"*16)

    for item in listaCompra:
       print(item)
     
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


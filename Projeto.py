listaCompra = []
entradaMenu = 0
adicionarItem = ""


#tratar o rerro de poder digitar uma letra
def Menu():
    global entradaMenu

    print("")
    print("-"*4)
    print("MENU")
    print("_"*4)

    print("\n1-Adicionar item à lista")
    print("2-Excluir item da lista")
    print("3-Mostrar lista")
    print("4-Sair")

    entradaMenu = int(input("\nInforme um número correspondente ao que deseja fazer:"))


"""
ARUMAR
contém bugs:

por conta da variável ser declarada como string (str) o programa permite:
1- Adionar múmeros
2- Prosseguir se o usuário não digitar nada
3- Adicionar caracteres
"""
def adicionar_item():
    global sequenciaItem
    sequenciaItem = 0

    print("")
    print("-"*16)
    print("ADIÇÃO DOS ITENS")
    print("-"*16)

    while True:
        sequenciaItem += 1 #Usada para a sequência dos números na lista

        adicionarItem = str(input(f"\n(Digite -1 quando quiser sair).{sequenciaItem}° item:")).capitalize()

        if not adicionarItem:
            print("Você não informou nenhuma palavra. Informe uma palavra")
            continue
        
        #Encerra a adição de itens  
        if adicionarItem == "-1":
            break

        #Adiciona à lista a sequência e os itens
        else:
            listaCompra.append(f"{sequenciaItem}-{adicionarItem}")

#problema: quando o item é removido os números não se atualizam para que a lista continue na sequência
def remover_item():

    mostrar_lista()

    print("")
    print("-"*17)
    print("REMOÇÃO DOS ITENS")
    print("-"*17)
    while True:

        try:
            removerItem = int(input(f"\n(Digite -1 quando quiser sair).Digite o número correspondente ao item que deseja remover:"))

            if removerItem == -1:
                break

            if removerItem == 0:
                print("\nVocê informou um número que não existe na lista. Tente novamente e informe um número que esteja na lista")
                continue

            numero = listaCompra[removerItem -1] #O índice que o usuário deseja remover é atribuido à variável na contagem humana

            
        except IndexError:
            print("\nVocê informou um número que não existe na lista. Tente novamente e informe um número que esteja na lista")

        except ValueError:
            print("Por favor informe um número")

        # Só remove o item se o índice informado existir na lista
        else:
            listaCompra.remove(numero) 
            print(f"\n{numero} Removido com sucesso!")
       
def mostrar_lista():

    print("")
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
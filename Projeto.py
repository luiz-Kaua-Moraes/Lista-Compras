import time

#PROBLEMA A SER RESOLVIDO:
#quando ou usuário tira um item da lista a lista não se atualiza então é remoido um outro valor 

#CORES
ERRO = "\033[0;31m" #Vermelho
SUCESSO = "\033[0;32m" #Verde
DICA = "\033[0;33m" #Amarelo

RESET = "\033[0m" #Reseta as cores

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

    try:
        entradaMenu = int(input("\nInforme um número correspondente ao que deseja fazer:"))
    except:
        print(f"{ERRO}Você não informou um número.{DICA}Você deve informar um número{RESET}")


"""
ARUMAR
contém bugs:

por conta da variável ser declarada como string (str) o programa permite:
1- Adionar números
3- Adicionar caracteres
4- Na príxima interação com esta seção a lista não continua a sequência e coloca como se fosse a primeira vez que o usuário entra com os dados
"""

def mensagem_voltando_menu(tempo):
    print("\nVontando para o Menu...")
    time.sleep(tempo)

def adicionar_item():
    global sequenciaItem
    sequenciaItem = 0 #Usada para a sequência dos números na lista

    print("")
    print("-"*16)
    print("ADIÇÃO DOS ITENS")
    print("-"*16)

    while True:
        sequenciaItem += 1 #Usada para a sequência dos números na lista

        adicionarItem = str(input(f"\n(Digite -1 quando quiser sair).{sequenciaItem}° item:")).capitalize()


        #Verifica se o usuário deu entrada com uma palavra
        if not adicionarItem:
            print(f"{ERRO}\nVocê não informou nenhuma palavra.{DICA}Você deve informar uma palavra{RESET}")
            sequenciaItem -=1 #diminui a seqência para que não continue sem o usuário não ter informado nada
            continue
        
        #Verifica se  entrada é -1 para que se ecerre a seção de adicionar item  
        if adicionarItem == "-1":

            mensagem_voltando_menu(3) #leva 3 segundo para voltar ao menu
            break

        #Adiciona na lista a sequência e os itens
        else:
            listaCompra.append(f"{sequenciaItem}-{adicionarItem}")
            print(f"{adicionarItem} {SUCESSO}Adicionado com sucesso!{RESET}")

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

            #Verifica se a entrada é -1 para da seção remover
            if removerItem == -1:
                break

            #Impede de ser digitado o zero porque ele nunca exitirá na lista
            if removerItem == 0:
                print(f"\n{ERRO}Você informou um número que não existe na lista. {DICA}Tente novamente e informe um número que esteja na lista{RESET}")
                continue

            numero = listaCompra[removerItem -1] #O índice que o usuário deseja remover é atribuido à variável na contagem humana

        #Trata o erro de número que não existe na lista
        except IndexError:
            print(f"{ERRO}\nVocê informou um número que não existe na lista. {DICA}Tente novamente e informe um número que esteja na lista{RESET}")

        #Trata o erro de entrada diferente de um número
        except ValueError:
            print(f"{ERRO}Você não informou um número. {DICA}Por favor informe um número{RESET}")

        # Só remove o item se o índice informado existir na lista
        else:
            listaCompra.remove(numero) 
            print(f"\n{numero} {SUCESSO}Removido com sucesso!{RESET}")
       
def mostrar_lista():

    print("")
    print("-"*16)
    print("LISTA DE COMPRAS")
    print("-"*16)

    #Verifica se tem item na lista
    if len(listaCompra) >0:
        for item in listaCompra:
            print(item)
        mensagem_voltando_menu(5)

    #Se não tiver iitem na lista volta para o menu
    else:
        print(f"{ERRO}Sua lista está vazia!{RESET}")
        mensagem_voltando_menu(3)

while True:
    Menu()
    match entradaMenu:
        case 1:
            adicionar_item()
        case 2:
            #verifica se a lista contém item
            if len(listaCompra) >0:
                remover_item()

            #Se não tiver item exibe uma mensegem
            else:
                print(f"\n{ERRO}Sua lista está vazia. {DICA}Para remover um item é necessário que tenha um item na sua lista{RESET}")
                mensagem_voltando_menu(4)
        case 3:
            mostrar_lista()
        case 4:
            time.sleep(5)
            print("Encerrando programa...")
            break
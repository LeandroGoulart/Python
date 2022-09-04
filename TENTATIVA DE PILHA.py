import os

def execFunction(function, value):
    if function == 1:
        list.append[value]

def menuType():         # Início do primeiro menu
    types = {
        1 : 'Fila',
        2 : 'Pilha'
    }
    correct = False

    while not correct:
        print ('Com que tipo de lista deseja trabalhar ?')

        for key in types:
            print(f"{key} - {types[key]}")

        try:
            typeList = int(input(''))
            types[typeList]
            correct = True
        except:
            print('Esolha novamente. Opção invalida!!')

    return types[typeList]


def menuOptions():             # Chamada da função de manipulação da lista
    correct = False    
    menuOptions = {
        1 : 'Adicionar número',
        2 : 'Excluír número',
        9 : 'Sair'
    }

    while not correct:
        print ('\n*****   MENU   *****\n')
        for key in menuOptions:
            print(f"{key} - {menuOptions[key]}")

        try:
            menuOption = int(input(''))
            menuOptions[menuOption]
            correct = True
            return menuOption
        except:
            print(os.system('cls'),'\nPor favor, Escolha uma das opções abaixo!!')
    

def addNumero(registro, list):  # Adicionar numero
    list.append(registro)
    

def removeNumero(registro, list, typeL):     # Remover numero
    match typeL:
        case 'Fila':
            list.remove(list[0])
        case 'Pilha':
            list.remove(list[len(list)-1])    

if __name__ == "__main__":          # Iniciando o programa
    
    # MOSTRA a opção de lista ou pilha
    list = []
    typeL = menuType()
    menuControl = None

    # PEGA a opção desejada
    while menuControl != 9:
        menuControl = menuOptions()

        os.system('cls')
        
        match menuControl:
            case 1:
                registro = input(f'Registro a ser inserido na {typeL} \n')    
                addNumero(registro, list)
            case 2:  
                if len(list) == 0:
                    print('OPAA!!! A LISTA JA ESTA VAZIA!!!\n')

                else:
                    removeNumero(registro, list, typeL)
        

        print(list)
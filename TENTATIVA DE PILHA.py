from ast import Import
import os


import os

menuOptions = {
1 : 'Adicionar número',
2 : 'Excluír número',
0 : 'Sair'
}

menu = None

list = []

def execFunction(function, value):
    if function == 1:
        list.append[value]

def menuType():
    correct = False
    typeList = None
    while not correct:
        types = {
        1 : 'Fila',
        2 : 'Pilha'
}

print ('Escola um tipo de lista ------')

for key in types:
    print(f"{key} - {types[key]}")

try:
    typeList = int(input(''))types[typeList]
correct = True
except:
print('Valor não definido!')

return typeList


def menuOptions():
    print ('Menu -----------------')
    print ('1 - Adicionar número')
    print ('2 - Excluír número')
    print ('0 - Sair')

def removeFila(fila):
    pass

while menu != 0:

    typeList = menuType()

# try:
# menu = int(input('Para utilizar o menu, insira uma opção numérica: \n'))
# except:
# os.system('clear')
# print('Digite uma opção válida.')

# try:
# execFunction(menuOptions[menu])
# except:
# os.system('clear')
# print('Opção não encontrada')
from time import sleep
from __future__ import annotations
from typing import List, Any

################   TRABALAHNDO A PILHA  ######################################
class Stack:
    """criar uma classe para fazer uma pilha"""

    def __init__(self) -> None:
        # Representa os itens da nossa stack
        self.__data: List[Any] = []
        # Representa o índice para iterações com for
        self.__index = 0

    def append(self, item: Any) -> None:
        """append da lista ORIGINAL"""
        self.__index += 1
        self.__data.append(item)

    def pop(self) -> Any:
        """ NÃO aceita índice"""
        return self.__data.pop()

    def peek(self) -> Any:
        """ NÃO elimina o topo da pilha"""
        if not self.__data:
            return []

        return self.__data[-1]

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__data})'

    def __iter__(self) -> Stack:
        self.__index = len(self.__data)
        return self

    def __next__(self) -> Any:
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]

    def __bool__(self) -> bool:
        return bool(self.__data)
#######################################################################

################   TRABALAHNDO A LISTA  ######################################
#######################################################################


############## Menu 2: Adicionar , excluir  e sair####################
def menu2():
    while


#######################################################################


#################### MENU PRINCIPAL#################################
opcao = 0
while opcao != 3:
    print ('Você deseja trabalhar com pilha ou fila?')
    print ('''       [1]FILA         [2]PILHA       [3]SAIR''') 
    opcao = int (input('Qual é a sua opção?'))
    if   opcao ==1:
        print('FILA')
    elif opcao ==2:  
        print('PILHA/n/n')
        
    elif opcao ==3: 
        print ('Finalizando ...  ...')    
    else:
        print('Opção inválida, por favor tente de novo.')
    print('***' *10)
    sleep(2)

print('Fim do programa !! Volte sempre.')
#######################################################################
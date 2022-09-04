import os
from time import sleep


################   TRABALHANDO A PILHA  ###########################

##################################################################


################   TRABALHANDO A LISTA  ###########################
###################################################################


############## Menu 2: Adicionar , excluir  e sair ################


####################################################################


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
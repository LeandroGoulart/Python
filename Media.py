import os

def pulalinha():
    print ('\n')
    print ('=-'*15)
    print ('\n')
    return 

os.system ('cls')

pulalinha() 

print ('Tirando a média')

nota1 =  float (input ('Digite a nota :  '))
nota2 =  float (input ('Digite a nota :  '))
nota3 =  float (input ('Digite a nota :  '))
nota4 =  float (input ('Digite a nota :  '))
media_ano = float ((nota1 + nota2 + nota3 + nota4)/4)
print ('\nO resultado da média é: {:.1f}'.format(media_ano))

pulalinha()

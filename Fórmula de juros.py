#traduzindo uma fórmula de juros compostos ao python
"""
Fórmula de juros composto
M=C(1+i)^t
M = montante
C = capital
i = taxa de juros
t = tempo
"""
C = int(input("Informe capital para investimento: "))
i = 15/1000
t = int(input("Tempo de aplicação em meses: "))
M=C*(1 + i)**t
print (M)

print ('Seu rendimento total será: ',M)
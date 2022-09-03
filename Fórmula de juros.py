#traduzindo uma fórmula de juros compostos ao python
"""
Fórmula de juros composto
M=C(1+i)^t
M = montante
C = capital
i = taxa de juros
t = tempo
"""
C = int(input("\nInforme capital para investimento: "))
i = 15/1000
t = int(input("\nTempo de aplicação em meses: "))
M=C*(1 + i)**t
print ('Juros de retorno= ',M-C)
res = "{:.2f}".format(M)
print ('Seu rendimento total será: ',res)
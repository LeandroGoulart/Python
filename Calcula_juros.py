#traduzindo uma fórmula de juros compostos ao python
"""
Fórmula de juros composto
M=C(1+i)^t
Legenda
M = montante
C = capital
i = taxa de juros
t = tempo
"""
C = float(input("\nInforme capital para investimento: "))
i = 15/1000
t = float(input("\nTempo de aplicação em meses: "))
M=C*(1 + i)**t
print ('\nJuros de retorno= ', M-C)
res = "{:.2f}".format(M)
print ('\nSeu rendimento total será: {} \n' .format(res)) 
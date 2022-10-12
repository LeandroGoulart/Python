#algoritmo para a sequencia de fibonacci

"""
recebe o numero anterior e soma ao proximo
"""
anterior =0
proximo =1
numeroAtual =3
print (anterior)
print (proximo)
while (numeroAtual <= 15):
#numero 15 é quantos numeros da sequencia voce deseja
  soma = anterior+proximo
  anterior = proximo
  proximo = soma
  print(proximo)
  numeroAtual +=1

'''Essa função recalcula aumento de salário.
Caso o funcionário receba até R$ 3000 reais, recebe 20% de reajuste
Acima de R$3000 reajusta 10% de reajuste '''

print ("Calcule o reajuste de salário anual")
print("Se o salário for menor que 3000 recebe reajuste 20%, caso contrário recebe reajuste de apenas 10%.")

valor = int (input ("Digite um valor: R$ "))

if valor<=3000:
  print("Valor com juros: R$ ", valor + (valor * 20 / 100))
else:print("Valor com juros: R$", valor + (valor * 10 / 100))
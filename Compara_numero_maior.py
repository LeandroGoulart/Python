import <system>
# exercício 1
print("Esse programa pede dois números e imprime o maior deles.")

# captura numero 1
num1 = int(input("Digite o primeiro número : "))

# captura numero 2
num2 = int(input("Digite o segundo número : "))
print(num1, num2)

# inicio função
if num1 > num2:
    print("O primeiro número é maior : ", num1)
elif num1 == num2:
    print("os dois números são iguais")
else:
    print("O número ", num2, " é maior que ", num1)

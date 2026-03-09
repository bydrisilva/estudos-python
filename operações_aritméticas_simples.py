# Operações Aritméticas Simples: Escreva um programa que peça dois números ao usuário e exiba a soma, subtração, multiplicação e divisão entre eles.
num1 = float(input("Digite o primeiro número: "))
#Criamos a variável, declaramos o tipo dela e usamos a função input para o usuário inserir os dados.
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
# Criamos a variável soma e realizamos uma operação entre os valores de duas variáveis que o usuário digitou.
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"A soma de {num1} e {num2} é: {soma}")
#Usamos o print para exibir na tela, o f-string para formatar a mensagem e as variáveis para mostrar os resultados das operações.
# {} é usado para chamar uma variável dentro do texto.
print(f"A subtração de {num1} e {num2} é: {subtracao}")
print(f"A multiplicação de {num1} e {num2} é: {multiplicacao}")
print(f"A divisão de {num1} e {num2} é: {divisao}")
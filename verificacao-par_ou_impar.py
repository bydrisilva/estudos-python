#Verificação de Número Par ou Ímpar: Peça ao usuário para digitar um número e informe se ele é par ou ímpar.
numero = input("Digite um número:")
numero = int(input("Digite um número: "))
# Aqui convertemos o dado do usuário que retorna em string para um número inteiro.
if numero % 2 == 0:
# % retorna o resto da divisão, então se o número for divisível por 2 o resultado será 0.
    print(f"O número {numero} é par.")
# Colocamos a variável dentro da frase para mostrar o dado.
else:
    print(f"O número {numero} é ímpar.")
# Se o resultado for diferente de 0 significa que é um número impar.
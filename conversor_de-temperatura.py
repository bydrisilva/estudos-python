# Conversor de Temperatura: Crie um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa.
celsius = float(input("Digite a temperatura em Celsius: "))
# Começamos declarando uma variável para armazenar a temperatura em Celsius digitada pelo usuário.
# FOI FEITA UMA PESQUISA!!!! Nela procuramos a fórmula para converter Celsius para Fahrenheit: F = (C * 9/5) + 32
# Exemplo: Se estiver 25°C em Brasília: 
# 25 X 1.8 = 45 |(9/5 = 1.8)
# 45 + 32 = fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
# Colocamos a fórmula para converter Celsius para Fahrenheit e armazenamos o resultado em uma variável chamada fahrenheit.
# Por fim, imprimimos o resultado para o usuário.
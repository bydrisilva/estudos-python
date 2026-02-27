# OPERADORES MATEMÁTICOS.

print("PLANEJAMENTO DA VIAGEM")
# Variáveis iniciais
distancia_km = 450         # Distância total da viagem.
consumo_moto = 30          # A moto faz 30 km por litro.
preco_gasolina = 5.50      # Preço de 1 litro de gasolina.

# 1. DIVISÃO (/): Quantos litros vamos gastar no total?
litros_necessarios = distancia_km / consumo_moto
print(f"1. Precisaremos de {litros_necessarios} litros de gasolina.")
#F usado para chamar a variável dentro do texto junto com as {}.

# 2. MULTIPLICAÇÃO (*): Quanto isso vai custar?
custo_gasolina = litros_necessarios * preco_gasolina
print(f"2. O custo da gasolina será R$ {custo_gasolina}")

# 3. ADIÇÃO (+): Adicionando o dinheiro do lanche na parada
custo_com_lanche = custo_gasolina + 45.00
print(f"3. Custo total com lanche: R$ {custo_com_lanche}")

# 4. SUBTRAÇÃO (-): Usando um cupom de desconto de 20 reais no posto!
custo_final = custo_com_lanche - 20.00
print(f"4. Custo final com desconto: R$ {custo_final}")

print("\n CRONOGRAMA DE PILOTAGEM")

# 5. DIVISÃO INTEIRA (//): Quantos trechos completos de 200km conseguimos fazer?
# A divisão inteira joga fora as casas decimais e te dá um número redondo.
trecho_maximo = 200
trechos_completos = distancia_km // trecho_maximo
print(f"5. Faremos {trechos_completos} trechos completos de 200km.")

# 6. MÓDULO (%): Quantos km sobram para o último trecho?
# O módulo ( % ) pega apenas o "resto" da divisão. 
# Ex: 450 dividido por 200 dá 2, e SOBRA 50. O módulo captura esse 50.
km_restantes = distancia_km % trecho_maximo
print(f"6. O trecho final terá {km_restantes} km.")
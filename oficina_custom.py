# EXERCÍCIO DE VARIÁVEIS.
# 1. CRIANDO AS VARIÁVEIS (Guardando os dados nas caixas).

modelo_moto = "Intruder 125" #STRING (Texto sempre deentro de "".)
ano_fabricacao = 2010 #INT (Número inteiro sem aspas.)
valor_investido = 4500.50 #FLOAT (Decimal, usa . ao invés de ,.)
projeto_finalizado = False #BOOBLEAN (Verdadeiro ou falso, sempre com a primeira letra MAIUSCULA)

# 2. ACESSANDO AS VARIÁVEIS (Olhando o que tem dentro da caixa).
print("FICHA DA OFFICINA.")
# Mostrará na tela a frase dentro das aspas. 
print(f"Modelo: {modelo_moto}")
#Aqui estamos chamando o nome da variável, fazemos isso com {} e o nome da mesma dentro.
# O nome da variável está dentro da frase mas não se torna uma frase por conta do f.
print(f"Ano:{ano_fabricacao}")
print(f"Total investido até agora: R${valor_investido}")

# 3. ALTERANDO O VALOR DA VARIÁVEL (A mágica de variar).
# Supomos que comprei um novo banco de couro e foi R$ 300 reais. 
# Vamos somar mais esse valor de gasto. 
valor_investido = valor_investido + 300.00

print("\n ATUALIZAÇÃO DO PROJETO")
print ("Nova peça comprada.")
print(f"Novo total investido de R$ {valor_investido}")
# TESTE DE TIPAGEM DINÂMICA (Os dados da variável podem ser modificados).

# 1. A caixa começa guardando um texto (string).
status_intruder = "Desmontada aguardando peças"
print("Fase 1:")
print(f"Conteúdo: {status_intruder}")
#F serve para dier que tem variável no texto, funciona me conjunto com {}.
#Aqui vai mostrar no terminal os dados da variável.
print(f"Raio-X do tipo: {type(status_intruder)}\n")
# Aqui vai mostrar no terminal o TIPO da variável.
# O que será impresso: Raio-X do tipo: <class 'str'>
# type é para saber o tipo de uma variável, funciona em conjunto com ().
# \N significa nova linha. \ acompanhada de algum caractere torna o mesmo diferente 

# 2. A MESMA caixa agora vai guardar um Número Inteiro (Int)
# Em C ou Java, isso aqui daria um erro fatal e travaria o programa!
status_intruder = 15
print("Fase 2:")
print(f"Conteúdo (Dias na oficina): {status_intruder}")
print(f"Raio-X do tipo: {type(status_intruder)}\n")

# 3. A MESMA caixa agora guarda um Verdadeiro/Falso (Boolean)
status_intruder = True
print("Fase 3:")
print(f"Conteúdo (Pronta para rodar?): {status_intruder}")
print(f"Raio-X do tipo: {type(status_intruder)}")
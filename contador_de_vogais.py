#Contador de Vogais: Receba uma frase do usuário e conte o número de vogais nela.

frase = input("Escreva aqui uma frase:")
# Começamos declarando uma variável para armazenar a frase digitada pelo usuário.
vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕàèìòùÀÈÌÒÙ"
# Criamos uma string contendo todas as vogais, tanto minúsculas quanto maiúsculas e com acentos, para facilitar a contagem.
contador = 0
# Declaramos uma variável contador para armazenar o número de vogais encontradas na frase, iniciando com zero.
# Zero pois ainda não contamos nenhuma vogal.
for letra in frase:
# Aqui começa um LAÇO DE REPETIÇÃO, onde vamos iterar sobre cada letra da frase digitada pelo usuário.
# O laço for percorre cada letra da frase, permitindo que verifiquemos se cada letra é uma vogal ou não.
# FOR É PERCORREDOR. O for é a ação de repetir o movimento de pegar "cada uma".
# IN É O CONTEÚDO. O in é onde está o conteúdo que iremos percorrer.
# Para cada letra, verificamos se ela é uma vogal comparando-a com a string de vogais que criamos.
    if letra in vogais:
        contador += 1
        # Só é executado se a letra for uma vogal. Se a letra for encontrada na string de vogais, incrementamos o contador em 1.
print(f"O número de vogais na frase é: {contador}")

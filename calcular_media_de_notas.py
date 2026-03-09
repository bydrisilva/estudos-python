# Calcular Média de Notas: Receba quatro notas de um aluno, calcule a média e exiba o resultado.
nota1 = float(input("Digite a primeira nota: "))
# Cada nota tem uma variável diferente para armazenar o valor.
# O input está pegando os dados e ele é convertido para floar para permitir os números decimais.
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
# Criamos uma nova variável chamada media que recebe os valores das variáveis notas e as divide por 4.
# / é o operador de divisão em Python.
print(f"A média do aluno é: {media}")
# O print exibe a média do aluno usando uma f-string para formatar a saída.
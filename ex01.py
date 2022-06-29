#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 1 - Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.
#
def menor(valor1, valor2):  # declarando a função
    if valor1 < valor2: # verificando se o primeiro valor é menor que o segundo valor
        print(f"O menor valor é {valor1}") # imprimindo o primeiro valor
    elif valor1 > valor2: # verificando se o primeiro valor é maior que o segundo valor
        print(f"O menor valor é {valor2}") # imprimindo o segundo valor
    else: # se os valores forem iguais
        print(f"{valor1} e {valor2} são iguais") # imprimindo que os valores são iguais (valor1 e valor2)


# testando a função com os valores passados pelo usuário
menor(10, 20) # imprimindo o menor valor (10)
menor(20, 10) # imprimindo o menor valor (10)
menor(10, 10) # imprimindo que os valores são iguais (10 e 10)

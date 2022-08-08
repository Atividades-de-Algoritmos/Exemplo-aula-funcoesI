#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 1 - Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def menor(valor1, valor2): # Declarando a função
    
    if valor1 < valor2: # Verificando se o primeiro valor é menor que o segundo valor
        print(f"O menor valor é {valor1}") # Imprimindo o primeiro valor
    
    elif valor1 > valor2: # Verificando se o primeiro valor é maior que o segundo valor
        print(f"O maior valor é {valor2}") # Imprimindo o segundo valor
    
    else: # Se os valores forem iguais
        print(f"{valor1} e {valor2} são iguais") # Imprimindo que os valores são iguais (valor1 e valor2)


# -- Chamada das funções --

menor(10, 20) # Imprimindo o menor valor (10)
menor(20, 10) # Imprimindo o menor valor (10)
menor(10, 10) # Imprimindo que os valores são iguais (10 e 10)

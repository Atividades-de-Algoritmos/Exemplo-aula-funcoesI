#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 2 - Escreva uma função que recebe um número n como parâmetro e imprime se n é nulo, positivo ou negativo.


def teste(valor1): # Declarando a função
  
  if valor1 < 0: # Verificando se o valor é menor que 0
    print(f"{valor1} é negativo") # Imprimindo que o valor é negativo (valor1)
  
  elif valor1 > 0: # Verificando se o valor é maior que zero
    print(f"{valor1} é positivo") # Imprimindo que o valor é positivo (valor1)
  
  else: # Se o valor for igual a 0
    print(f"{valor1} é nulo") # Imprimindo que o valor é nulo (valor1)


# -- Chamada das funções --

teste(10) # Imprimindo que o valor é positivo (10)
teste(-10) # Imprimindo que o valor é negativo (-10)
teste(0) # Imprimindo que o valor é nulo (0)

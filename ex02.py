#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 2 - Escreva uma função que recebe um número n como parâmetro e imprime se n é nulo, positivo ou negativo.

# declarando a função
def teste(valor1):
  if valor1 < 0: # verificando se o valor é menor que 0
    print(f"{valor1} é negativo") # imprimindo que o valor é negativo (valor1)
  elif valor1 > 0:
    print(f"{valor1} é positivo") # imprimindo que o valor é positivo (valor1)
  else: # se o valor for igual a 0
    print(f"{valor1} é nulo") # imprimindo que o valor é nulo (valor1)


# testando a função com os valores passados pelo usuário
teste(10) # imprimindo que o valor é positivo (10)
teste(-10) # imprimindo que o valor é negativo (-10)
teste(0) # imprimindo que o valor é nulo (0)

#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 2 - Escreva uma função que recebe um número n como parâmetro e imprime se n é nulo, positivo ou negativo.

def verifica_valor(n): # Declarando a função
  
  if n < 0: # Verificando se o valor é menor que 0
    print(f"\n{n} é negativo") # Imprimindo que o valor é negativo (n)
  
  elif n > 0: # Verificando se o valor é maior que zero
    print(f"\n{n} é positivo") # Imprimindo que o valor é positivo (n)
  
  else: # Se o valor for igual a 0
    print(f"\n{n} é nulo") # Imprimindo que o valor é nulo (n)


# -- Chamada das funções --

verifica_valor(n = float(input('Informe o valor: '))) # Chamando a função teste passando como parâmetro um valor flutuante solicitado do usuário

print('\nFim do programa ') # Informando ao usuário que o programa chegou ao fim
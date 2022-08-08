#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 3 - Escreva um aplicativo calculadora, ele deve solicitar ao usuário as entradas de valores e qual a operação a realizar.

# -- Declarando as funções --

def somar(valor1 : float, valor2 : float): # Função soma, recebendo dois valores flutuantes.
    return valor1 + valor2 # retornar a soma entre os dois valores.

def subtrair(valor1 : float, valor2 : float): # Função subtrair, recebendo dois valores flutuantes
    return valor1 - valor2 # retornar a subtração entre dois valores

def multiplicar(valor1 : float, valor2 : float): # Função multiplicar, recebendo dois valores flutuantes
    return valor1 * valor2 # retornar a multiplicação entre dois valores

def dividir(valor1 : float, valor2 : float): # Função dividir, recebendo dois valores flutuantes
  
  if valor2 == 0: # Se o segundo parâmetro informado for igual a 0
    return "Não é possível dividir por zero" # Retorna uma mensagem de erro ao usuário
  
  else: # Caso contrário
    return valor1 / valor2 # Retorna o valor da divisão entre o valor1 e valor2

# -- Criando um menu de opções no console --

operacoes = {'+': somar, '-': subtrair, '*': multiplicar, '/': dividir} # Dicionário com as opções do menu e as funções correspondentes

numero1 = int(input("Digite o primeiro número: ")) # Solicitando um valor inteiro e armazenando na variável numero1
numero2 = int(input("Digite o segundo número: ")) # Solicitando um valor inteiro e armazenando na variável numero2

print("\nOperadores disponíveis;\n") # Imprimindo no console os operadores disponíveis

for i in operacoes: # Percorrendo o dicionário dos operadores disponíveis e imprimindo no console
  print(i) # Imprimindo os valores do dicionário

opcao = input("\nDigite a operação desejada: ") # Solicitando a operação do usuário

# -- Chamada das funções --

funcao = operacoes[opcao] # Buscando no dicionário a opção informada

resultado = funcao(numero1, numero2) # Chamando a função buscada no dicionário

print(f"{numero1} {opcao} {numero2} = {resultado}") # Imprimindo no console o resultado da operação

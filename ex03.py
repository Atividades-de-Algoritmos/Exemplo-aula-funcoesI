#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 3 - escreva um aplicativo calculadora, ele deve solicitar ao usuário as entradas de valores e qual a
# operação a realizar.

# declarando as funções
def somar(valor1, valor2):
    return valor1 + valor2

def subtrair(valor1, valor2):
    return valor1 - valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2

def dividir(valor1, valor2):
  if valor2 == 0:
    return "Não é possível dividir por zero"
  else:
    return valor1 / valor2

# criando um menu de opções
# dicionário com as opções do menu
operacoes = {'+': somar, '-': subtrair, '*': multiplicar, '/': dividir}

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("Digite a operação desejada:")
for i in operacoes:
  print(i)

opcao = input("Digite a operação desejada: ")
funcao = operacoes[opcao]
resultado = funcao(numero1, numero2)
print(f"{numero1} {opcao} {numero2} = {resultado}")

# ou
print("-" * 20)
print("ou calculas todas as operações")

for operacao in operacoes:
  print(f"{operacao} = {operacoes[operacao](numero1, numero2)}")


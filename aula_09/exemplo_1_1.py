"""
Operadores Relacionais - Aula 4
== > >= < <= !=
"""
#Igualdade ==
num_1 = 2 #int
num_2 = '2' #string

print(num_1 == num_2)

num_3 = 2 #int
num_4 = 2 #int

expressao = (num_3 == num_4)

print(expressao)

#Maior que >
num_3 = 3 #int
num_4 = 2 #int

expressao = (num_3 > num_4)

print(expressao)

#Maior igual >=
num_3 = 2 #int
num_4 = 2 #int

expressao = (num_3 >= num_4)

print(expressao)

#Menor que <
num_3 = 3 #int
num_4 = 2 #int

expressao = (num_3 < num_4)

print(expressao)

#Menor igual <=
num_3 = 2 #int
num_4 = 2 #int

expressao = (num_3 <= num_4)

print(expressao)

#Diferente de !=
num_3 = 3 #int
num_4 = 2 #int

expressao = (num_3 != num_4)

print(expressao)


nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

#Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO PODE PEGAR O EMPRÉSTIMO!')




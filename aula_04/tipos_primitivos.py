"""
Tipos de dados
str - string - textos 'Assim' ou "Assim"
int - inteiro - 123 - 0 - -10 - 50 - 100
float - real/ponto flutuante - 10.50 - 1.5 - -10.03
bool - boleano/lógico - True / False
"""

print('Gui', type('Gui'))
print(10, type(10))
print(10.5, type(10.5))
print(10 == 10, type(10 == 10))

#typecasting

print('nome', type('nome'), bool('luiz'))

print('10', type('10'), type(int('10')))

#contatenando
print('10' + '10')

# String: nome
print('Guilherme', type('Guilherme'))
# Idade: int
print('30', type(30))
# Altura: float
print('1.80', type(1.80))
#É maior de idade:
print(30 > 18, type(30 > 18))

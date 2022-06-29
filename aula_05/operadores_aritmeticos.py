"""
Operadores Aritméticos

+ soma
- subtraçõa
* multiplicação
/ divisão
// divisão inteira
** exponenciação
% resto da divisão
() precedencia matemática
"""

print("Soma", 10 + 10)
print("Multiplicação", 10 * 10)
print("Subtração", 10 - 5)
print("Divisão", 10 / 2)

# Multiplicação de String
print("Multiplicação * ", 10 * "A")

#Concatenação
print("Guilherme" + " " + "Akinyele " + str(30) + " anos")
print("Gabrielli" + " " + "Cunha")

#Operações de float com int
print(10.5 // 3)

#Divisião Inteira
print(10 // 3)

#Potência
print("Potenciação", + 10 ** 2)

#Resto da operação
print("Operação sem resto", + 10 % 5)
print("Operação com resto", + 10 % 3)

#Precedencia
print("Sem parenteses", + 5+2*10)
print("Com parenteses", + (5+2)*10)

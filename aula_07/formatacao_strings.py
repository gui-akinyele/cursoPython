nome = "Guilherme"
idade = 30 #int
altura = 1.80 #float
e_maior = idade > 18 #booleano
peso = 80
imc = peso / (altura **2)

print(nome, 'tem ', idade, 'anos de idade e seu IMC é de', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

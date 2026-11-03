# Desafios

# 1- Crie um programa que leia dois números e mostre a soma entre eles. 
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print (f'A soma entre {n1} e {n2} é: {s}')

# 2 - Faça um programa que leia algo pelo teclado e mostre na tela qual o seu tipo primitivo e todas as informações possíveis sobre ela. 
tipo = input('Digite uma palavra: ')
print('É numérico?', tipo.isnumeric())
print('É alfabético?', tipo.isalpha())
print('É alfanumérico?', tipo.isalnum())
print('Está em minúsculas?', tipo.islower())
print('Está em maiúsculas?', tipo.isupper())

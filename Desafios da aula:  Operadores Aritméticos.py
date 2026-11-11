# 1- Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor
n1 = int(input('Digite um número:'))
ant = n1 - 1 
suc = n1 + 1
print(f'O antecessor de {n1} é {ant} e seu sucessor é {suc}')

# 2- Cire um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um número:'))
dobro = n1 * 2   
triplo = n1  * 3 
raiz =  n1**(1/2)
print(f'O dobro de {n1} é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz}')

# 3- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua méida
n1 = int(input('Prova 1:'))
n2 = int(input('Prova 2:'))
n3 = int(input('Prova 3:'))
med = (n1+n2+n3)/3
print (f'Resultado: {med}')

# 4- Escreva um programa que leia um valor em metros e o exiba convertido em milímetros e centímetros 
m = int(input('Metro: '))
c = m*100
ml = m*1000
print (f'o metro {m} equivale a {c} em centímetroe e {ml} em milímetros ')

# 5- Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada 
n = int(input('Digite um numúero do 1 ao 10:'))
n1 = n*1
n2  = n*2
n3  = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8  = n*8
n9 = n*9
n10 = n*10
print(f'Tabuada do número{n}: \n {n} x 1 = {n1} \n {n} x 2 = {n2} \n {n} x 3 = {n3} \n {n} x 4 = {n4} \n {n} x 5 = {n5} \n {n} x 6 ={n6} \n {n} x 7 = {n7} \n {n} x 8 = {n8} \n {n} x 9 = {n9} \n {n} x 10 = {n10}')

# 6- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela terá.
n = int(input('Digite o valor presente em sua conta bancária em real:'))
d = n/5
print(f'você possui {d} em dólares')

# 7- Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print(f'A parede tem a dimensão de {larg} x {alt} e sua área é de {area}.')
tinta = area/2
print(f'Para pintar essa parede você precisa de {tinta}L de tinta')'

# 8- Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preço = float (input('Digite o preço do produto: R$'))
novo = preço - (preço*5/100)
print(f'O produto que custava {preço}, na promoção, com desconto de 5% vai custar R$ {novo}')

# 9- Faça um algorítimo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento.
 

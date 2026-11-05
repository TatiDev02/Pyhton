# Operadores aritiméticos em python:

#1- Exponenciação ** = 2 ** 3	 
#2- Multiplicação * = 4 * 3
#3-  Divisão / = 10 / 4
#4- Divisão Inteira // = 10 // 4
#5- Módulo % = 10 % 4
#6 -Adição  + = 5 + 3
#7- Subtração - = 5 - 3

#  ordem de precedência dos operadores em Python

#1- Parênteses =  (): Tudo dentro deles é resolvido antes
#2- Exponenciação (Potência) = **  
#3- Sinais Unários (Positivo/Negativo) = +x, -x
#4- Multiplicação, Divisões e Resto = *, /, //, %
#5- Adição e Subtração = +, -



# Macete caso queira encontrar a raiz quadrada de um número 
print(81**(1/2))
print(25**(1/2))
print(36**(1/2))
print(49**(1/2))

# formas de espaçãmento/posição da string:
 
nome=input('Qual o seu nome?')
print(f'Muito prazer, {nome:20}!')
#Qual o seu nome?Tati
#Muito prazer, Tati                !
#PS C:\Users\Thiago\Desktop\python> 

nome = input('Qual o seu nome?')
print(f'Muito prazer, {nome:>20}!')
#Qual o seu nome?Tati
#Muito prazer,                 Tati!
#PS C:\Users\Thiago\Desktop\python> 

nome = input('Qual o seu nome?')
print(f'Muito prazer, {nome:<20}!')
#Qual o seu nome?Tati
#Muito prazer, Tati                !
#PS C:\Users\Thiago\Desktop\python> ^C

nome = input('Qual o seu nome?')
print(f'Muito prazer, {nome:^20}!')
#Qual o seu nome?Tati
#Muito prazer,         Tati        !
#PS C:\Users\Thiago\Desktop\python> 

nome = input('Qual o seu nome?')
print(f'Muito prazer, {nome:=^20}!')
#Qual o seu nome?Tati
#Muito prazer, ========Tati========!
#PS C:\Users\Thiago\Desktop\python>  

# adição em python indicado pelo curso
n1 =int(input('Um valor:'))
n2 = int(input('Outro valor:'))
print (f'A soma vale{n1+n2}')

# Outros opradores explorados pelo curso:
n1 =int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2
print(f'a soma é: {s}, a multiplicação é: {m} e a divisão é: {d}')
print(f'Divisão inteira: {di} e potência: {e}')

#Um valor:8
#Outro valor:2
#a soma é: 10, a multiplicação é: 16 e a divisão é: 4.0
#Divisão inteira: 4 e potência: 64
#PS C:\Users\Thiago\Desktop\python> ^C

# \n -> usado para quebra de texto
n1 =int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2
print(f'a soma é: {s} \n  a multiplicação é: {m} \n a divisão é: {d}')
print(f'Divisão inteira: {di} \n potência: {e}')

# end=' ' -> usado para não haver quebra de texto
n1 =int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2
print(f'a soma é: {s}  a multiplicação é: {m} e a divisão é: {d}', end=' ')
print(f'Divisão inteira: {di} e potência: {e}', end=' ')

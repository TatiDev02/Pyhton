# resolução da atividade anterior:
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número'))
s=n1+n2
print(f'A soma vale, {s}')

# Exemplos de tipos primitivos explicados no curso
# int: 7, -4, 0, 9875
# float: 4.5, 0.075, -15,223, 7,0
# bool: true/false
#" str: 'olá'. '7.5'

# Veja o seguinte código abaixo considerando que a aula informa aimportância dos tipos primitivos e sua relação com a saída de dados:
 n1=input ('Digite um valor:')
print (type(n1))
# nota: o comando type serve para que o cósigo mencione a classificação do input solicitado ao usuário. 

# No terminal, o comando seria interpretado da seguinte forma:
#PS C:\Users\Thiago\Desktop\python> & "C:\Program #Files\Python311\python.exe" #"c:/Users/Thiago/Desktop/python/Respondendo ao #Usuário.py"
#Digite um valor:5
#<class 'str'>
#PS C:\Users\Thiago\Desktop\python>

# Nota: o valor declarado deveria ser classificado com um número inteiro, não como uma string 
# isso confirma o fato de que o tipo primitivo de uma variável deve ser especificada.

# Agora, se inserirmos o comando primitivo int, a resposta do terminal se torna correta:
n1= int (input ('Digite um valor:'))
print (type(n1))

# PS C:\Users\Thiago\Desktop\python> & "C:\Program #Files\Python311\python.exe" #"c:/Users/Thiago/Desktop/python/Respondendo ao #Usuário.py"
#Digite um valor:5
#<class 'int'>
#PS C:\Users\Thiago\Desktop\python> 

#veja outro exemplo refente a importância da classificação dos tipos primitivos das variáveis:

n1 = input('Digite um valor:')
n2 = input('Digite outro valor:')
s = n1 + n2
print ('A soma vale', s)

#PS C:\Users\Thiago\Desktop\python> & "C:\Program #Files\Python311\python.exe" #"c:/Users/Thiago/Desktop/python/Respondendo ao #Usuário.py"
#Digite um valor:5
#Digite outro valor:5
#A soma vale 55
#PS C:\Users\Thiago\Desktop\python

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print ('A soma vale', s)

#PS C:\Users\Thiago\Desktop\python> & "C:\Program #Files\Python311\python.exe" #"c:/Users/Thiago/Desktop/python/Respondendo ao #Usuário.py"
#Digite um valor:5
#Digite outro valor:5
#A soma vale 10
#PS C:\Users\Thiago\Desktop\python> 

# Desafio do curso: 
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print (f'A soma entre {n1} e {n2} é: {s}')

#PS C:\Users\Thiago\Desktop\python> & "C:\Program #Files\Python311\python.exe" #"c:/Users/Thiago/Desktop/python/Respondendo ao #Usuário.py"
#Digite um valor:5
#Digite outro valor:5
#A soma entre 5 e 5 é: 10
#PS C:\Users\Thiago\Desktop\python> 



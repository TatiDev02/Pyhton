# desafio: 1- Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas - vindas de acordo com o valor digitado. 
nome = input ("Olá! Qual é o seu nome?")
print("Seja bem-vindo(a)", nome )

# desafio: 1- outra forma de responder com o uso da função  f-string atribuída ao símbolo {}
nome = input ("Olá! Qual é o seu nome?")
print(f"Seja bem-vindo(a), {nome}!")

# desafio: 2 - Crie um script python que leia o dia, mês e o ano de nascimento de uma pessoa e mostra a mensagem com a data fornecida
dia_nascimento = input ("Digite o número do dia em que você nasceu (ex:25,08,10...)")
mes_nascimento = input("Digite o mês de seu nascimento (ex: janeiro, fevereriro...)")
ano_nascimento = input("Digite o ano de seu nascimento com quatro algarismos(ex: 1984,2007...)")
print("Ficha:", dia_nascimento, mes_nascimento, ano_nascimento)
 
# desafio: 3 - Crie um script que leia dois números e tente mostrar a soma entre eles
numero_um = input ("Digite um número:")
numero_dois = input("Digite outro número:")
print("a soma entre:", numero_um, "e:", numero_dois, "é:", int(numero_um) + int(numero_dois))

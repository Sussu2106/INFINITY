#1
'''
Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem informando que ele foi multado. Além disso, calcule o valor da multa que irá custar R$ 70,00 por cada km passado acima do limite.
'''

velocidade_carro = int(input("Digite a velocidade do carro em km/h: "))
limite_velocidade = 80
valor_multa = 70

if velocidade_carro > limite_velocidade:
    km_excedidos = velocidade_carro - limite_velocidade
    valor_multa = km_excedidos * valor_multa

    print(f"Velocidade {km_excedidos} km/h.")
    print(f"Você foi multado. O valor da multa é de{valor_multa}.")
else:
    print("Sem multa!")


    
#2
'''Faça um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.''''
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


#3
'''
Faça um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem do ônibus, cobrando R$ 0,85 por cada km rodado para viagens de até 200 km e R$ 0,57 para viagens com mais de 200 km
'''
distancia = float(input("Digite a distância da viagem em quilômetros: "))

ate_200 = 0.85
acima_200 = 0.57

if distancia <= 200:
    preco_passagem = distancia * ate_200
else:
    preco_passagem = distancia * acima_200

print(f"O preço da passagem é de R$ {preco_passagem}")


#4
'''
Faça um programa que leia um ano qualquer e mostre se ele é ou não bissexto. Pesquise as condições que fazem um ano ser ou não bissexto.
'''
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

#5
'''Faça um programa que leia dois números e mostre qual é o maior e o menor deles'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
	print(f'O número {num1} é o maior')
	print(f'O número {num2} é o menor')
elif num2 > num1:
    print(f'O número {num2} é o maior')
    print(f'O número {num1} é o menor')
else:
    print('Os números são iguais')


#6
'''Faça um algoritmo que pergunte o salário de um funcionário e calcule o novo salário com aumento. Para salários de até R$ 1320,00, o aumento será de 15% e para salários superiores a R$ 1320,00 o aumento será de 10%.
'''
sal = float(input('Informe o salário: '))
aum1 = sal * 1.15
aum2 = sal * 1.10

if sal > 1320:
	print(f'O salário com aumento é de: R${aum2}')
else:
	print(f'O salário com aumento é de: R${aum1}')
        
#7
'''Desenvolva um programa que leia o comprimento de três retas e mostre se elas podem ou não formar um triângulo. DICA: Pesquise quais as condições de três retas formarem um triângulo.'''
lado1 = int(input('Informe o tamanho do lado1: '))
lado2 = int(input('Informe o tamanho do lado2: '))
lado3 = int(input('Informe o tamanho do lado3: '))

if lado2 - lado3 < lado1 < lado2 + lado3 and lado1 - lado3 < lado2 < lado1 + lado3 and lado1 - lado2 < lado3 < lado1 + lado2:
	print(f'Os lados {lado1}cm, {lado2}cm e {lado3}cm formam um triângulo')
else:
	print('Os lados informados não formam um triângulo')
        

#8
'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo'''
valor = int(input("Digite um valor: "))

if valor > 0:
    print(f"{valor} é positivo.")
elif valor < 0:
    print(f"{valor} é negativo.")
else:
    print(f'{valor} é igual a zero.')


#9
'''Faça um Programa que leia um número e em seguida mostre se o número é:
inteiro ou decimal;
positivo ou negativo;
par ou ímpar, somente se o número for inteiro e positivo
'''
#usar float para testar casa decimal!
numero = float(input("Digite um número: "))


if numero == int(numero):
    print("O número é inteiro.")
else:
    print("O número é decimal.")

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")

if numero == int(numero) and numero > 0:
    if int(numero) % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

#10
'''Faça um Programa que verifique se uma letra digitada é "A". Conforme a letra escrever: “A de amor”, “Letra inválida :(“
'''
letra = input("Digite uma letra: ")

if letra == "A":
    print("A de amor")
else:
    print(f"{letra} não é de amor")


'''
#11
#pesquisar
'''



#12
'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#13
'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool - R$ 3,80 por litro
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina R$ 4,70 por litro
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente. 
'''
'''
alcool = 3.80
gasolina = 4.70
litros = float(input("Digite o número de litros:"))
tipo = input("Digite o tipo de combustível (A-álcool/G-gasolina): ").upper()

if tipo == "A":
    if litros <= 20:
        valor_total = litros * (alcool - alcool * 0.03)
    else:
        valor_total = litros * (alcool - alcool * 0.05)
elif tipo == "G":
    if litros <= 20:
        valor_total = litros * (gasolina - gasolina * 0.04)
    else:
        valor_total = litros * (gasolina - gasolina * 0.06)
else:
    print(f"O valor a ser pago é: R$ {valor_total}")??????
'''


#14
'''Faça um programa que faça 5 perguntas de sim ou não para uma pessoa sobre um crime.'''
'''
print("Responda as perguntas abaixo com 'sim' ou 'não':")
pergunta1 = input("Fez a matrícula na Infinity? ")
pergunta2 = input("Está treinando programação além da sala de aula? ")
pergunta3 = input("Fez o teste de lógica? ")
pergunta4 = input("Entrega as atividades em dia? ")
pergunta5 = input("Tá aprendendo a programar pelos dedos? ")

'''




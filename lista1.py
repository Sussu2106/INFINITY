#1
print ('Hello World')

#2
a = input('Digite um número')
n1 = int(a)+ 1
n2 = int(a)- 1
print (f'O número {a} tem o antecessor {n1} e o sucessor {n2}')

#3
b = input('Digite um número')
print (f'O número digitado foi {b}')

#4
c = float(input('Digite o primeiro número'))
d = float(input('Digite o segundo número'))
soma = c + d
print(soma)

#5
e = float(input('Digite a nota'))
f = float(input('Digite a nota'))
g = float(input('Digite a nota'))
h = float(input('Digite a nota'))
media = (e + f + g + h)/4
print(media)

#6
i = float(input('Digite a metragem'))
centimetros = i / 100
print (centimetros)

#7
j = float(input('Valor do produto'))
desconto = (j * 0.05)
total = (j - desconto)
print (f'O valor do produto com o desconto de 5% é de {total}')

#
#
#10
k = int(input('Quanto você ganha por hora?'))
l = int(input('Quantas horas você trabalha por mês?'))
soma = k * l
print (f'Mensalmente você ganha {soma}')

#11
m = float(input("Quantos graus ºF fazem agora?"))
converter = 5 * ((m-32)/9)
print(f'Fazem {converter} graus ºCelsius')

#12
n = int(input('Digite um número'))
o = int(input('Digite outro número'))
oo = float(input('Digite o último número'))
p = (2 * (n))
q = ((o)/2)
print(f'{p + q}')
print(f'{n * 3 + oo}')
print(f'{oo ** 3}')

#13
r = int(input('Digite sua altura em centímetros'))
s = ((72.7 * (r / 100))-58)
print(f'Peso ideal para uma pessoa de {r/100} é de {s}KG')

#14
mb = int(input('Tamanho de arquivo em MB'))
mbps = int(input('Velocidade de link Mbps'))
bites = (mb*8*1024*1024)
tempo = bites/(mbps*1024*1024)
minutos = (tempo/60)
print(f'O tempo aproximado de download é de {bites} minutos')


#15
v = int(input('Quantas você ganha por hora?'))
x = int(input('E trabalha quantas horas por mês?'))
bruto = (v*x)
inss = ((bruto/100)*8)
sindicato = ((bruto/100)*5)
ir = ((v*x/100)*11)
resto = (bruto - sindicato - ir)
print(f'Salário bruto{bruto}')
print(f'Parte paga ao INSS{inss}')
print(f'Pago ao sindicato{sindicato}')
print(f'Desconto {ir}')
print(f'Salário Líquido {resto}')

#16
cobertura_litros_metro= 1 / 3
capacidade_lata_litros = 18
preco_lata = 80.00

#metros quadrados
tamanho_area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
litros_necessarios = tamanho_area * cobertura_litros_metro
quantidade_latas = (litros_necessarios / capacidade_lata_litros)
preco_total = quantidade_latas * preco_lata
print(f"Quantidade de latas de tinta a serem compradas: {quantidade_latas}")
print(f"Preço total a ser pago: R$ {preco_total:.2f}")


#17???

#18

idade = int(input('Informe sua idade em dias'))
anos = int(idade/365)
meses = int(anos/12)
dias = int(meses/30)
print(f'Você possui {anos} anos, {meses} meses e {dias} dias.')

#19


#20
numero = int(input('Poe um número aí'))
aa = (numero * 1)
bb = (numero * 2)
cc = (numero * 3)
dd = (numero * 4)
ee = (numero * 5)
ff = (numero * 6)
gg = (numero * 7)
hh = (numero * 8)
ii = (numero * 9)
jj = (numero * 10)
print(f'{aa}\n{bb}\n{cc}\n{dd}\n{ee}\n{ff}\n{gg}\n{hh}\n{ii}\n{jj}')


#21
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

#22
numero = int(input("Digite um número de 0 a 9999: "))
unidades = numero % 10
dezenas = (numero // 10) % 10
centenas = (numero // 100) % 10
milhares = (numero // 1000) % 10

print(f"Unidades: {unidades}")
print(f"Dezenas: {dezenas}")
print(f"Centenas: {centenas}")
print(f"Milhares: {milhares}")


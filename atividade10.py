lista = ["limão", "laranja", "maracujá", "abacaxi", "mexerica"]
fruits = input('Digite um nome de uma fruta')
fruta = fruits
if fruta in lista:
    print(f'{fruta} está na lista!')
else:
    print('A fruta informada não está na lista')
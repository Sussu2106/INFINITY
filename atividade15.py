frase = input('informe uma frase')
espaco = 0
for letra in frase:
    if letra.isspace():
        espaco += 1
print(f'A palavra {frase} tem {espaco} espaços!')
        
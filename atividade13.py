palavra = input('informe uma palavra')
vogal = 0
for letra in palavra:
    if letra in "aeiou":
        vogal += 1
print(f'A palavra {palavra} tem {vogal} vogais!')
        
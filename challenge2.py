def vowels_text(texto):
    vogais = 0
    for letra in texto:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1
    print('The number of vowels is ' + str(vogais))

texto = input('Enter a message ')
vowels_text(texto)
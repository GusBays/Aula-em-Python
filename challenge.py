text ='We are having a great time in polisinos. There are vey smart students here'

vogais = 0
consoantes = 0

for letra in text:
    if letra in 'aeiouAEIOU':
        vogais += 1
    elif letra not in (' ','.',','):
        consoantes = consoantes + 1

print('Number of vowels in the text is ' + str(vogais))
print('Number of consonants in the text is ' + str(consoantes))

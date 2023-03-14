import random

n1 = ('FELICIDADE')
n2 = ('TRISTEZA')
n3 = ('NOJO')
n4 = ('RAIVA')
n5 = ('MEDO')

emocoes = [n1, n2, n3, n4, n5]
escolha2 = random.choice(emocoes)


f1 = (f'Eu sinto {escolha2} quando... ')
f2 = (f'Eu reajo a emoção de {escolha2} fazendo...')
f3 = (f'Quando eu sinto {escolha2} meu corpo fica...')
f4 = (f'Quando eu sinto {escolha2}, me dá vontade de...')
f5 = (f'Quando eu sinto {escolha2}, eu não devo...')
f6 = (f'Quando meu amigo sente {escolha2}, eu...')

frases = [f1, f2, f3, f4]
escolha1 = random.choice(frases)


print(escolha1)

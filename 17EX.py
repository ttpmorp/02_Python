'''
17.  FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE
DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
'''
import math

co = float(input('Digite o valor do cateto OPOSTO: '))
ca = float(input('Digite o valor do cateto ADJACENTE: '))

h = co ** 2 + ca ** 2
print(f'O valor da hipotenusa é de {math.sqrt(h)}')

'''
15. ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO POR UM CARRO ALUGADO
E A QUANTIDADE DEDIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE CARRO
CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.
'''

d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

d = d * 60
km = km * 0.15

print(f'O total a pagar é R${d + km:.2f} ')

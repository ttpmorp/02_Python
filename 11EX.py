'''
11. FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA,
PINTA UMA ÁREA DE 2M**2.
'''

l = float(input('Digite a LARGURA da sua parede: '))
a = float(input('Digite a ALTURA da sua parede: '))

area = l * a

print(f'Sua parede tem dimensão {l} x {a} e a sua área é de {area}m²')

tn = (area / 2)

print(f'Você irá precisar de de {tn}L de tinta para pintar esta parede!')


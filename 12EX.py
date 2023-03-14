'''
12. FAÇA UM ALGORITIO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM
5% DE DESCONTO.
'''

v = float(input('Qual o valor do produto? '))

d = (v * 5)/100

print(f'Você terá um desconto de {d}, logo o valor do seu produto será de {v - d}')


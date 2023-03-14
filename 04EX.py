"""
4. FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA RELA O SEU TIPO PRIMITIVO E TODAS
AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

"""

n = input('Digite algo: ')

print(type(n))

print(f'É numérico? {n.isnumeric()}')
print(f'É decimal? {n.isdecimal()}')
print(f'É alfa? {n.isalpha()}')
print(f'Está em minúsculo? {n.islower()}')
print(f'Está em maiúsculo? {n.isupper()}')
print(f'É apenas espaço em branco? {n.isspace()}')


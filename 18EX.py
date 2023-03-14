from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo de uma circunferência (ou seja, entre 0º e 360º) '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'O VALOR DE SEN É IGUAL A {sen} DE TANGENTE É IGUAL A {tan} e de conseno é {cos}')


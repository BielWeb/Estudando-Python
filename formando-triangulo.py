r1 = int(input('Digite o primeiro número: '))
r2 = int(input('Digite o segundo número: '))
r3 = int(input('Digite o terceiro número: '))
if r1 - r2 < r3 < r1 + r2:
    print('Com esses valores você consegue formar um triângulo!')
else:
    print('É impossível formar um triângulo')

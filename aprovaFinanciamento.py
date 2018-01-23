print('----------------APROVADOR DE FINANCIAMENTO----------------')
#Pedindo dados do usuário
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu rendimento mensal: '))
anos = int(input('Digite em quantos anos será financiada a casa: '))
#Fazendo calculos
meses = anos * 12
prestacao = valor / meses
print('Você vai pagar {:.2f} por mês durante {} meses'.format(prestacao, meses))
if prestacao > salario * 0.30:
    print('\033[31mEMPRÉSTIMO NEGADO! Você não tem condições de financiar essa casa!')
else:
    print('EMPRÉSTIMO APROVADO! Você consegue pagar a casa!')

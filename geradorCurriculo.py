print('---------GERADOR DE CURRÍCULOS---------')
#declaracao de variaveis - INICIO
nome = str(input('Nome completo: '))
ano = int(input('Ano de Nascimento: '))
prof = str(input('Sua profissão: '))
end = str(input('Seu endereço: '))
fone = str(input('Seu telefone: '))
email = str(input('Seu email: '))
curso1 = str(input('Digite um curso: '))
escola1 = str(input('Onde você fez o 1º Curso?'))
duracao1 = str(input('Duração do primeiro curso(em horas/aula): '))
curso2 = str(input('Digite outro curso: '))
escola2 = str(input('Onde você fez o 2º Curso?'))
duracao2 = str(input('Duração do segundo curso(em horas/aula): '))
emprego1 = str(input('Digite um emprego: '))
empresa1 = str(input('Nome da empresa: '))
tempo1 = str(input('Quanto tempo você passou?(meses) '))
emprego2 = str(input('Digite outro emprego: '))
empresa2 = str(input('Nome da empresa: '))
tempo2 = str(input('Quanto tempo você passou?(meses) '))
#declaracao de variaveis - FIM
#geracao de curriculo
print('\n')
print('\033[36m//////////////////DADOS PESSOAIS//////////////////')
print('\033[34mNOME: {}'.format(nome.upper()))
#condicioanal idade - INICIO
if 2018-ano < 18:
    print('{} ANOS - ESTAGIÁRIO'.format(2018-ano))
else:
    print('{} ANOS'.format(2018-ano))
#condicional idade - FIM
print('PROFISSÃO: {}'.format(prof.upper()))
print('Reside em {}'.format(end))
#condicional contato - INICIO
if email != '':
    print('Telefone: {}  /  Email: {}\n\n'.format(fone, email))
else:
    print('Telefone: {}\n\n'.format(fone))
#condicional contato - FIM
print('\033[36m//////////////////////CURSOS//////////////////////')
#condicional cursos - INICIO
if curso1 != '' and escola1 != '' and duracao1 != '':
    print('\033[34m{} | {} | Duração: {} horas/aula'.format(curso1,escola1,duracao1))
if curso2 != '' and escola2 != '' and duracao2 != '':
    print('{} | {} | Duração: {} horas/aula'.format(curso2, escola2, duracao2))
#condicional cursos - FIM
print('\033[36m///////////EXPERIÊNCIAS PROFISSIONAIS///////////')
#condicional empregos - INICIO
if emprego1 != '' and empresa1 != '' and tempo1 != '':
    print('\033[34mCargo: {} | Empresa: {} | Duração: {} meses'.format(emprego1, empresa1, tempo1))
if emprego2 != '' and empresa2 != '' and tempo2 != '':
    print('\033[34mCargo: {} | Empresa: {} | Duração: {} meses'.format(emprego2, empresa2, tempo2))
#condicional empregos - FIM

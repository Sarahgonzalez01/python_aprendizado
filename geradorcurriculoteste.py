# gerador de curriculos - próprio para treinar a lógica
#variaveis
habilidades_lista = []
nome = input('Digite seu nome completo: ')
data_nascimento = (input ('Digite sua data de nascimento: '))
endereco = input ('digite seu endereço completo: ')
email = input ('digite seu e-mail:')
objetivo = input ('Digite seu objetivo: ')
formacao = input ('Digite sua primeira formação acadêmica e ano de conclusão: ')
formacao2 = input ('Digite sua segunda formação acadêmica e ano de conclusão: ')

print ('\n Selecione abaixo quantas habilidades deseja por no seu curriculo ')
print ('\n Uma habilidade')
print ('\n Duas habilidades')
print ('\n 3 habilidades')
print ('\n 4 habilidades')

numero = input('Escolha uma opção de (1 a 4): ')

if numero == '1':
    habilidade1 = input ('digite sua habilidade: ')
    print ('habilidade adicionada: ', habilidade1)
    habilidades_lista.append(habilidade1)

elif numero == '2':
    habilidade1 = input ('Digite sua primeira habilidade: ')
    habilidade2 = input ('Digite sua segunda habilidade: ')
    print ('Habilidade 1 adicionada:', habilidade1)
    print ('Habilidade 2 adicionada: ', habilidade2)
    habilidades_lista.append([habilidade1, habilidade2])

elif numero == '3':
    habilidade1 = input ('digite sua primeira habilidade: ')
    habilidade2 = input ('digite sua segunda habilidade: ')
    habilidade3 = input ('Digite sua terceira habilidade: ')
    print ('habilidade 1 adicionada: ', habilidade1)
    print('Habilidade 2 adicionada: ', habilidade2)
    print ('habilidade 3 adicionada: ', habilidade3)
    habilidades_lista.extend([habilidade1, habilidade2, habilidade3])
elif numero == '4':
    habilidade1 = input('Digite sua primeira habilidade: ')
    habilidade2 = input ('Digite sua segunda habilidade: ')
    habilidade3 =  input ('Digite sua terceira habilidade: ')
    habilidade4 = input ('Digite sua quarta habilidade: ')
    print('habilidade 1 adicionada: ', habilidade1)
    print('Habilidade 2 adicionada: ', habilidade2)
    print('habilidade 3 adicionada: ', habilidade3)
    print('habilidade 4 adicionada: ', habilidade4)
    habilidades_lista.extend([habilidade1, habilidade2, habilidade3, habilidade4])
else:
    print ('Isto é invalido')
  #-------------------------------------------------------------------------------
#montando a estrutura para receber as informações

print (f'{nome}\n'.upper())
print (f'Nascimento: {data_nascimento}')
print(f'Endereço {endereco}')
print (f'E-mail: {email}\n')
print (f'objetivo\n {objetivo}\n')
print (f'Formação\n {formacao} \n {formacao2}\n')
print (f'Habilidades:\n ')
for habilidade in habilidades_lista:
    print(f'- {habilidade}')


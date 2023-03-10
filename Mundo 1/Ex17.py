valida = True
while valida:
    sexo = input('Digite seu sexo: ').upper()
    if sexo == 'F':
        print('Sexo Feminino')
    elif sexo == 'M':
        print('Sexo Masculino')
    else:
        #valida = False
        print('Digite seu sexo novamente: ')



numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado. Não adicionado.')
    r = str(input('Deseja continuar: [S/N]'))
    if r in 'Nn':
        break
print(f'Os numeros adicionados na lista foram: {numeros}')

    


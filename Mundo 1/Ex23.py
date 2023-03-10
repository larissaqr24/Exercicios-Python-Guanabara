import random
cont=0
while True:
    num = random.randint(1,100)
    input('VAMOS JOGAR PAR OU ÍMPAR!!!')
    numero = int(input('Diga um valor: '))
    soma = numero + num
    par_impar = input('Par ou ímpar[P/I]: ').upper()
    print(f'Você jogou {numero} e o computador {num}. A soma foi {soma}.') 
    if soma % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    
    if result == par_impar:
        cont+=1
        print(f'Voce ganhou!! Total de {cont} vitorias consecutivas')
    else:
        print('GAME OVER!!!')
        break
    print('---' * 30)


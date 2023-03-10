num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
while True:
    op = int(input('Informe a opção do menu: '))
    if op == 1:
        soma = num1 + num2
        print(soma)
    elif op == 2:
        mult = num1 * num2
        print(mult)
    elif op == 3:
        if num1 > num2:
            print(f'O número maior é o {num1}')
        else:
            print(f'O número maior é o {num2}')
    elif op == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite um novo número: '))
    elif op == 5:
        print(Saindo do Programa.)
        break
print('=='*10)
input('BANCO CEV')
print('=='*10)
valor_saque = int(input('Qual valor você quer sacar: '))
c50 = 0
c20 = 0
c10 = 0
c1 = 0
restante = valor_saque
while restante > 0:
    if restante >= 50:
        restante = restante - 50
        c50 += 1
    elif restante >= 20:
        restante = restante - 20
        c20 += 1
    elif restante >= 10:
        restante = restante - 10
        c10 += 1
    elif restante >= 1:
        restante = restante - 1
        c1 += 1 
print(f'Você vai precisar de {c50} nota de cédula 50.')
print(f'Você vai precisar de {c20} notas de cédulas 20.')
print(f'Você vai precisar de {c1} notas de cédulas 1.')
print(f'Você vai precisar de {c10} notas de cédulas 10.')
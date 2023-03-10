# calcula a soma de número impares que são multiplos de 3 de 1 a 500.
soma = 0 
cont = 0 
for num in range (1, 501, 2):
    if num % 3 == 0:
             soma = soma + num
             #cont = cont + 1
             cont+=1 
print(f'A soma de todos os {cont} valores solicitados é : {soma}')


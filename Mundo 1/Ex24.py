contador_idade = 0
contador_homens = 0
contador_mulheres = 0
while True:
    idade = int(input('Qual é sua Idade: '))
    sexo = input('Qual é seu sexo: ').upper()

    if idade > 18:
        contador_idade +=1

    if sexo == 'M':
        contador_homens +=1 

    elif sexo == 'F' and idade < 20:
        contador_mulheres +=1 

    c = input('Você quer continuar? ').upper()
    if c == 'NAO':
        break

print(f'Maiores de 18 anos: {contador_idade}')
print(f'Homens cadastrados foram: {contador_homens}')
print(f'Mulheres abaixo de 20 anos: {contador_mulheres}')

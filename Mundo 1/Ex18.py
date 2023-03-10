import random

num = random.randint(1,10)
n = -1
print(num)

while n != num:
    n = int(input('Digite um número: '))

print(f'Você acertou! O numero era {num}')
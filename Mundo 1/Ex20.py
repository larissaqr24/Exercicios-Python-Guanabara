from typing import Counter


num = int(input('Fatorial de: '))
# 5! = 5x4x3x2x1 =120
resultado = 1
count = 1
while count <= num:
    resultado *= count
    count += 1
    print(resultado)
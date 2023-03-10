# Codigo para o exercicio
lista = []
for x in range(5):
    n = int(input("Digite um número: "))
    for chave, valor in enumerate(lista):
        if n < valor:
            lista.insert(chave, n)
            break
    else:
        lista.append(n)
    
print(lista)

# codigo se fosse no mundo real
'''lista = []
for x in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

lista.sort()
print(lista)'''
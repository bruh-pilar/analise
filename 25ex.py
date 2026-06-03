numeros=input("Digite os números separados por espaço: ").split()
print(numeros)
for numero in numeros:
    numero_inteiro = int(numero)
    print(f"numeros inteiros {numero_inteiro} ")
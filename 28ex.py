
numero = int(input("Digite o valor da tabuada: "))
print(f"\n--- TABUADA DO {numero} ---")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
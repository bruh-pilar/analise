nota=0 
while nota>= 0 and nota <= 10:
    try:
        nota = int(input("Digite uma nota entre 0 e 10:"))
    except ValueError:
        print("entrada invalida . Por favor, digite um numero")
print(f"nota invalida registrada :{nota}")        

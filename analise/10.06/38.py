def mostra_maior(valor1, valor2):
    if valor1 > valor2:
        print(f'o valor é:{valor1}')
    elif valor2> valor1:
        print(f'o valor é:{valor2}')
    else:
        print(f'os dois valores iguai')
v1=int(input("digite um valor"))
v2=int(input("digite outro valor"))
x= mostra_maior(v1, v2)
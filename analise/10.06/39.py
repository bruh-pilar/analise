def calcule_imc(peso, altura):
    imc= peso /(altura**2)
    if imc < 18.5:
        classe="magrelo(ª)"
    elif imc < 25:
        classe= "normal"
    elif imc < 30:
        classe= "sobrepeso"
    elif imc <= 35:
        classe= "obesidade 1"
    elif imc <= 39.9:
        classe="obesidade 2"
    else:
        classe="obesidade 3"
    return classe
seu_peso = float(input('Digite seu peso'))
sua_altura= float(input('Digite sua altura:'))
resultado = calcule_imc(seu_peso,sua_altura)
print(f" seu resultado é {resultado}")
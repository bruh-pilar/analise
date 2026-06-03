for numero in range (0, 11):
    linha = ""
    for multiplicador  in range (2 , 8):
        resultado= numero * multiplicador 
        linha +=f"{multiplicador} x{numero:2d} ={resultado:2d}| "
print(linha)
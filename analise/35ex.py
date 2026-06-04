while True:
    nome= input("digitar um nome ou escreva sair para parar)")
    if nome.upper() == "SAIR":
        print("saindo do programa")
        break
    if nome!= nome.upper():
        print("erro escrever em maiusculo")
    else:
        print(nome)    
        
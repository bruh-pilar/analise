nasc= int(input("Digite ano do seu nascimento "))
ano= int(input("Digite ano atual "))
idade= ano - nasc 
if idade >= 18:
    print("Maior de idade ")
else:
    print("menor de idade")
n1= float(input("digite a primeira nota "))
n2= float(input("digite segundo nota "))
media= (n1 + n2) /2
if media > 7:
    print("aprovado com a ",{media})
elif media == 5 or media == 6:
    print ("recuperação com a ", {media})
else:
    print("reprovado com a ",{media})


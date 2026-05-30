
fds=str(input('digite o dia da semana:')).upper()
hora= int(input("Qual horario?"))

if fds == "SEXTA" and hora==21:
    print ("Sextou! Você merece 1 chopp")
elif fds == "SEXTA" and hora ==22:
    print("Sextou! Você merece pelo menos 2 chopps")
else:
    print("Ainda não sextou! Não saia da rotina, e vá estudar")    

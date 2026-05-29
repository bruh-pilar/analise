##Enunciado do Exercício: Operação "Sextou"
#Uma universidade quer ajudar os estudantes a controlarem as expectativas para o final de semana 
#com base nos horários de término das aulas. Escreva um programa em Python que determine se o aluno
#já pode celebrar o fim da semana útil ou se ele deve continuar focado nos estudos.
#Requisitos do Programa:
#Entrada de Dados:
#Solicite ao usuário o dia da semana atual (ex: "sexta", "sábado", "segunda"). Dica: certifique-se de que o programa 
#aceite a resposta de forma independente de letras maiúsculas ou minúsculas.
#Solicite ao usuário a hora em que a aula finaliza, utilizando obrigatoriamente o formato de 24 horas (ex: 21, 22).
#Regras de Negócio e Saídas:
#Se o dia for "sexta" e o horário de término for exatamente 21h, exiba a mensagem:
#"Sextou! Você merece 1 chopp"
#Se o dia for "sexta" e o horário de término for exatamente 22h, exiba a mensagem:
#"Sextou! Você merece pelo menos 2 chopps"
#Para qualquer outro dia da semana, ou para qualquer outro horário na sexta-feira que não sejam os citados acima,
# o programa deve exibir uma mensagem motivacional de foco:
#"Ainda não sextou! Não saia da rotina, e vá estudar"##

fds=str(input('digite o dia da semana:')).upper()
hora= int(input("Qual horario?"))

if fds == "SEXTA" and hora==21:
    print ("Sextou! Você merece 1 chopp")
elif fds == "SEXTA" and hora ==22:
    print("Sextou! Você merece pelo menos 2 chopps")
else:
    print("Ainda não sextou! Não saia da rotina, e vá estudar")    
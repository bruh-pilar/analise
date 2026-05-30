"""Uma empresa precisa automatizar o cálculo do salário líquido de seus funcionários com base no cargo que 
ocupam e nas deduções de impostos (INSS e IRRF). Escreva um programa em Python que receba o cargo de um
 colaborador e realize os cálculos descritos a seguir.

Cargo         Salário Bruto
Caixa         R$ 1.500,00
Vendedor      R$ 2.400,00
Gerente       R$ 4.000,00

Qualquer outro cargo	R$ 0,00 (Exibir mensagem: "Não trabalha aqui")

Cálculo dos Descontos:
INSS: O desconto do INSS é fixo em 12% sobre o salário bruto para todos os cargos válidos.
IRRF (Imposto de Renda): A alíquota varia conforme o salário bruto:
Se o salário bruto for maior que R$ 2.000,00, o desconto é de 14%.
Caso contrário (menor ou igual a R$ 2.000,00), o desconto é de 8%.

Saída de Dados:
Ao final, o programa deve exibir de forma organizada as seguintes informações:
O Salário Bruto inicial.
O valor descontado de INSS.
O valor descontado de IRRF.
O Salário Final (Salário Líquido) após todas as deduções.
"""


def calcular(): 
    cargo=(input("Digite seu cargo?(caixa, vendedor, gerente)")).lower()
    if cargo== "caixa":
        salbruto= 1500
    elif cargo== "vendedor":
        salbruto= 2400
    elif cargo== "gerente":
        salbruto=4000
    else:
        print("Não trabalha aqui")
        return

    inss= salbruto*0.12
    if salbruto >2000:
        irrf=salbruto *0.14
    else:
        irrf= salbruto * 0.08
    salliquido = salbruto - inss - irrf
    print("\n"+"="*30)
    print(f"Desconto iss: R${salbruto:.2f}")
    print(f"desconto irrf:R$ {irrf:.2f}")
    print(f"salario liquido:R${salliquido:.2f}")
calcular()


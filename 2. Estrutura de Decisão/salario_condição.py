#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00



valor_hora = int(input('Digite aqui seu ganho por hora'))
horas_mes = int(input('Diga quantas horas vc trabalha por mes'))
salario = valor_hora * horas_mes
inss = (salario)-(salario -salario * 0.1)
ir = 0
fgts = (salario) - (salario - salario * 0.11)
percent = 0
salario_liquido = salario  - inss
inss = (salario)-(salario - salario * 0.1)


if salario > 900 and salario < 1500:
    ir = (salario - salario * 0.05)
    percent = "5%"
elif salario > 1500 and salario < 2500:
    ir = (salario - salario * 0.10)
    percent = "10%"
elif salario > 2500:
    ir = (salario - salario * 0.20)
    percent = "20%"

 

print("     Salário Bruto: (",valor_hora,"*",horas_mes,")        : R$",valor_hora * horas_mes)
print(
    "     (-)IR (",percent,")                      : R$",salario - ir
    )

print("     (-)INSS (10%)                      : R$",inss)


print ( "       FGTS (11%)                       : R$",fgts)

print ("Total de Descontos                      : R$", (salario - ir) + inss)
print("Salario liquido                         : R$",salario_liquido)

















#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
gain_hora = int(input("Colloque aqui eu ganho por hora"))
horas_mes = int(input("Coloque aqui quantas horas voce trabalha por mes"))
salario_mes = gain_hora * horas_mes
ir = (11/100) * salario_mes
inss = (8/100) * salario_mes
sindicato = (5/100) * salario_mes
salario_liquido = salario_mes - ir - inss - sindicato

print("Seu salario mensal é de R$",salario_mes)
print("+ Sala Brt : R$",salario_mes,)
print("- IR (11%) : R$",ir)
print("- INSS(8%) : R$",inss)
print("- Sind(5%) : R$",sindicato)
print("= Sala liq : R$",salario_liquido)

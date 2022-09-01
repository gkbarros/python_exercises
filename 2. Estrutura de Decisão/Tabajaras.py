#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = int(input("Coloca teu salario aqui que te dou o ajuste"))
percent = 0
if salario < 280:
    salario_2 = salario + salario * 0.2
    percent = "20%"
elif salario  > 280 and salario < 700:
    salario_2 = salario + salario * 0.15
    percent = "15%"
elif salario > 700 and salario < 1500:
    salario_2 = salario + salario * 0.1
    percent = "10%"
else:
    salario_2 = salario + salario * 0.05
    percent = "5%"

print("Esse é seu salario atual",salario,"Esse é seu salario apos o rejuste",salario_2,"A variação percentual foi de",percent,"O aumebto total foi de",salario_2 - salario)
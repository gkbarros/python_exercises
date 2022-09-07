#Faça um programa que receba a temp média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

year_mean = 0
temp = []
up_mean = {}
mouths = [
    'January','February','March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
    ]#teste pep8

for i in range(len(mouths)):
    temp.append(float(input('Type enter the year_mean temperature for ' + mouths[i] + ":")))
    year_mean += temp[i]
year_mean /= len(mouths)

for i in range(len(mouths)):
    if temp[i] > year_mean:
 	    up_mean.update({mouths[i] : temp[i]})

print('Mean of yearly temp  ' + str(year_mean))
print('Months with above year_mean temp' + str(up_mean))   
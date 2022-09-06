#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
from statistics import mean


mean =[]
seven_mean= 0

for students in range (10):
    grades_sum = 0
    for grade in range(4):
        print("Type",grade+1,"ª nota do", students+1,"º aluno")
        grades_sum += float(input())
    
    mean.append(grades_sum/4)

    if (grades_sum / 4) >= 7:
        seven_mean += 1

print(mean)
print("A total of ",seven_mean," students scored 7 or more")
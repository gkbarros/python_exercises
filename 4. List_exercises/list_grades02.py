#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
average =[]
seven_average= 0

for students in range (10):
    grades_sum = 0
    for grade in range(4):
        print("Type",grade+1,"ª nota do", students+1,"º aluno")
        grades_sum += float(input())
    
    average.append(grades_sum/4)

    if (grades_sum / 4) >= 7:
        seven_average += 1

print(average)
print("A total of ",seven_average," students scored 7 or more")
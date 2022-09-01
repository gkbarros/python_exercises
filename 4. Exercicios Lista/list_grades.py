#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
print("Give me your grades and i will give you the average!")
grades = []
n = 0
average = 0

for i in range(4):
    grades.append(float(input("Your grades here")))
    average = average + grades[i]
    n = n + 1
average = average / n
print(average)
print(grades)
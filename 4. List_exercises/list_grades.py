#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
print("Give me your grades and i will give you the mean!")
grades = []
n = 0
mean = 0

for i in range(4):
    grades.append(float(input("Your grades here")))
    mean = mean + grades[i]
    n = n + 1
mean = mean / n
print(mean)
print(grades)
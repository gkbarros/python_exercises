#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
age = []
height = []

for person in range(5):
    age.append(input("Type here your age"))
    height.append(input("Type here your height:"))

age.reverse()
height.reverse()
print(age)
print(height)
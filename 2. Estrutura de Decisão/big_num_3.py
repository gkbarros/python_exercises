#Faça um Programa que leia três números e mostre o maior e deles.

print ("Me de 3 numeros e te direi o maior e o menor")
num1 = int(input("Digite o primeiro numero aqui: "))
num2 = int(input("Digite o segundo numero aqui: "))
num3 = int(input("Digite o terceiro numero aqui: "))
#verificando o menor
menor = num1
if num2 < num1 and num2<num3:
    menor = num2
if num3 < num1 and num3<num2:
    menor = num3

print("O menor numero é o",menor)
#verificando o maior
maior = num1
if num2 > num1 and num2>num3:
    maior = num2
if num3 > num1 and num3>num2:
    maior = num3
print("O maior número é o",maior)
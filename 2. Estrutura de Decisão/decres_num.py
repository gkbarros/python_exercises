#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input('Primeiro numero: '))
num2  = int(input('Segundo numero : '))
num3 = int(input('Terceiro numero: '))

if num1 > num2 > num3:
    print(num1,num2,num3)
if num1 > num3 > num2:
    print(num1,num3,num2)
if num2 > num1 > num3:
    print(num2,num1,num3)
if num2 > num3 > num2:
    print(num2,num3,num1)
if num3 > num2 > num1:
    print(num3,num2,num1)
if num3 > num1 > num2:
    print(num3,num1,num2)
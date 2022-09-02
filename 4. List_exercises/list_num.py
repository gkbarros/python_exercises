#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
odd =[]
even = []
counter = 0
print("Give me 20 numbers and I'll tell you which are even and which are odd")
while counter != 20:
    num = int(input("Type a number here:"))
    counter += 1
    if (num % 2) == 0:
        even.append(num)
    else:
        odd.append(num)
print(f'You typed a total of {len(even)} even numbers.Here they are:{even}')
print(f'You typed a total of {len(odd)} odd numbers.Here they are:{odd}')


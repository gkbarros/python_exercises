#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
a = []
b = []
sum = 0 
for num in range(10):
    a.append(int(input("Add a number here:")))

for num in a:
    b.append(num ** 2)
for num in b:
    sum += num

print(b)
print(sum)
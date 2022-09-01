#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
list_number = []
for num in range(1,6):
    list_number.append(float(input("Enter a number here:")))
list_number.reverse()
print("Your numbers")
print("---------------")
print((list_number))
print("---------------")
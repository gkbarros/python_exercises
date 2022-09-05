#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
num_list =[]
sum = 0
mtl = 1
for num in range(5):
    num_list.append(int(input("Type here your numbers :")))

for num in num_list:
    sum += num
    mtl *= num

print(sum)
print(mtl)
print(num_list)
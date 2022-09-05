#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
list1 = []
list2 = []
list3 = []
i = 0
for num in range(2):
    for num in range (10):
        if i <= 9:
            list1.append(int(input("Type de first list here :")))
            i += 1
        else:
            list2.append(int(input("Type your second list here :")))
for num in range(10):
    list3.append(list1[num])
    list3.append(list2[num])

print(list1)
print(list2)
print(list3)
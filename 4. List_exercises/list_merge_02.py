#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
list1 = []
list2 = []
list3 = []
list4 = []
i = 0
for num in range(3):
    for num in range (10):
        if i <= 9:
            list1.append(int(input("Type de first list here :")))
            i += 1
        elif i<= 19:
            list2.append(int(input("Type your second list here :")))
            i+=1
        else:
            list3.append(int(input("Type your final numbers here :")))

for num in range(10):
    list4.append(list1[num])
    list4.append(list2[num])
    list4.append(list3[num])

print(list1)
print(list2)
print(list4)
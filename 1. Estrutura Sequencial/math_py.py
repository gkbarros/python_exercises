#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A. O produto do dobro do primeiro com metade do segundo .
#B. A soma do triplo do primeiro com o terceiro.
#C. O terceiro elevado ao cubo.
print("Oi me de 2 numeros inteiros e 1 numero real")
num_int_1 = int(input("Primeiro numero inteiro aqui:"))
num_int_2 = int(input("Bota aqui o segundo inteiro:"))
num_real = float(input("Agora, coloque aqui seu numero Real:"))
a = (num_int_1 * 2) * (num_int_2 / 2)
print("O produto do dobro do primeiro com metade do segundo é:",a)

b = (num_int_1 * 3) + (num_real)
print("A soma do triplo do primeiro com o terceiro dá:",b)

c = num_real ** 3
print("O terceiro elevado ao cubo dá:",c)

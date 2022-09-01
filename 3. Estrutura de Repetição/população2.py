#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input("População da cidade A"))
b = int(input("População da cidade B"))
ta = float(input("Taxa de crescimento da cidade A"))
tb = float(input("Taxa de crescimento da cidade B"))
ano = 0

while a <= b:
    a = a + (a * (ta/100))
    b = b + (b * (tb/100))
    ano = ano + 1

print(ano)
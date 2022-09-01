#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print("Me de uma letra que direi se é vogal ou consoante")
letra = input("Bota aqui a letra: ")
vogal = "aeiou"
if letra in vogal:
    print("A letra'",letra,"'é uma vogal")
else:
    print("A letra",letra,"é uma consoante")


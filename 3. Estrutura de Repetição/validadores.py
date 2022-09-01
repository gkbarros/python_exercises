#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Coloque aqui o nome:"))
while (len(nome)<=3):
    nome = str(input("Nome deve conter mais de 3 letras tente novamente"))

idade = int(input("Coloque aqui a idade:"))
while idade < 0 or idade >150:
    idade = int(input("Idade invalida tente novamente:"))

salario = int(input("Coloque aqui o salario:"))
while salario < 0:
    salario = int(input("Salario invalido, tente novamente"))

sexo = str(input("Coloque aqui o sexo:"))
while sexo != "F" and sexo != "M":
    sexo = str(input("Invalido, tente novamente:"))

estado_civil = input("Coloque aqui o estado civil:")
while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    estado_civil = input("Invalido, coloque novamente:")

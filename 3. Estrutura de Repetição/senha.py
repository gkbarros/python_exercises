#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Coloque aqui seu usuario :")
senha = input("Coloque aqui sua senha :")

while senha == usuario:
    print("Senha não pode ser igual ao usuario.")
    print("Preencha os campos novamente")
    usuario = input("Usuario:")
    senha = input("Senha:")

print(usuario,senha)
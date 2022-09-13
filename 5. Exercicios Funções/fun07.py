#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def cont(num):
    num = input("Type num here:")
    num_cont = list(num)
    print('The number ' + str(num) + ' has a total of : ' + str(len(num_cont))+ ' characters')
    return num

cont(0)
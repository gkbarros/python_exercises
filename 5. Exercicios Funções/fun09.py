#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random
#dado1 = [
#    1, 2, 3,
#    4, 5, 6
#    ]
#dado2 = [
#    1, 2, 3,
#    4, 5, 6
#    ]
#ponto = [
#    4, 5, 6,
#    8, 9, 10
#    ]
#result_dado1 = 0
#result_dado2 = 0
#resul = 0
#def craps():
#    result_dado1 = random.choice(dado1)
#    print('Primeiro dado :'+str(result_dado1))
#    result_dado2 = random.choice(dado2)
#    print('Segundo dado :'+str(result_dado2))
#    resul = result_dado1 + result_dado2
#    print('Seu jogo é de : '+str(resul))
#    if resul == 7 or resul == 11:
#        print("Parabéns você é um natural e ganhou o jogo.")
#    elif resul == 2 or resul == 3 or resul == 12:
#        print('Crap, you lost bro!')
#    for i in ponto:
#        if resul == i:
#            ponto_num = i
#            print('Seu ponto é '+ str(i)+' tireo novamente para ganhar, 7 vc #perde')
#            r = input('digite "Go" para jogar os dados novamente')
#            while r == "Go":
#                if ponto_num == 7:
#                    print('Deu 7 perdeu')
#                    break
#                elif resul == ponto_num:
#                    print('Ganhou o jogo, tirou '+str(resul)+' de novo!!')
#                    break
#                elif resul != ponto[i]:
#                    print('Deu '+str(resul)+' jogue de novo')
#            else:
#                r = print('Comando incorreto, deseja sair ? Tecle "exit" #para sair e "Go" para jogar os dados"')
#                
#craps()
#Jogo de Craps. Faca um programa de implementação de jogo de Craps. O jogador

# lanca um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,

# voce tirar7 ou 11, voce tirou um "natural" e ganhou. Se voce tirar 2, 3 ou

# 12 na primeira jogada, isto e chamado de "craps" e você perdeu. Sena

# primeira jogada, voce fez um 4, 5, 6, 8, 9 ou 10,este e seu "Ponto". Seu

# objetivo agora e continuar jogando os dados ate tirar este numero novamente.

# Voce perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

# Dica: para simular o lancamento do dado, utilize os métodos Random do Python.!
a = "Você ganhou, parabéns\n"

b="\n\n\t***** Craps! *****\n\nVocê perdeu!!!\tTente de novo\n"

c="Ponto\n"

def craps():

    dado1=random.randrange(1,7)

    dado2=random.randrange(1,7)

    soma=dado1+dado2

    print("Dado 1: ",dado1)

    print("Dado 2: ",dado2)

    print("A soma dos dados é: ",soma,"\n")

    return soma

    print("*****GAME - CRAPS*****")

while True:

        jogar=input("Rolar dados (s ou n)? ")

        if jogar=='n' or jogar=='N':
        
           break
       
        else:
        
           result=craps()

        if result==7 or result==11:
        
           print(a)

        elif result==2 or result==3 or result==12:
        
           print(b)

        else:
        
           print(c)

        while True:
        
           result2=craps()

           if result==result2:
        
               print(a)

               break
           
           elif result2==7:
        
               print(b)

               break
           
           else:
        
               print("Ainda não foi dessa vez!\nSEGUE O JOGO!!!!\n")
craps()
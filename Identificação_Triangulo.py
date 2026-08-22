#Definição de Looping final, caso o usuário queira recomeçar o programa após o término

continuar = "s"
while continuar in ("s","sim","y","yes"):

    print("Identificar tipos de triângulo...")

 #Looping para notificar o usuário caso ele digite algum comando incompatível
    while True:

        try:
            lado1 = float(input("Insira o lado 1 do triângulo: "))
            lado2 = float(input("Insira o lado 2 do triângulo: "))
            lado3 = float(input("Insira o lado 3 do triângulo: "))
            break

        except:
            print("Digite o apenas números")

#Regras para identificação do tipo do triângulo

    if lado1 == lado2 and lado1 == lado3:
        print("Seu triângulo é equilatero")

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Seu triângulo é escaleno")

    else:
        print("Seu triângulo é isósceles")

#Perguntar ao usuário caso ele quer reiniciar o programa
    continuar = input("Deseja identificar outro tipo de triângulo?")
    while continuar not in ("s","sim","y","yes","nao","não","n","no"):
        print("Comando não identificado... tente novamente")
        continuar = input("Deseja identificar outro tipo de triângulo?")

#Caso o usuário não queira identificar outro triângulo, o programa encerra.
print("PROGRAMA FINALIZADO....")
# Definição de Looping final, caso o usuário queira descobrir se outros anos são bissextos
continuar = "s"
while continuar in ("s","sim","y","yes"):

    print("Identificar se os anos são bissextos...")
# Looping para notificar o usuário caso ele digite algum comando incompatível

    while True:

        try:

            ano = int(input("Digite o ano que deseja saber: ").strip())
            break

        except:

            print("Digite apenas número inteiro")

#Regras para identificação de ano bissextos

    if ano%4 == 0 and ano%100 != 0:
        print("O ano adicionado é BISSEXTO (366 dias)")

    else:
        print("O ano adicionado é NORMAL (365 dias))")

#Perguntar ao usuário caso ele queira adicionar outro ano e fazer o looping ser válido
    continuar = input("Deseja descobrir se outro ano é bissexto?")
    while continuar not in ("s","sim","y","yes","nao","não","n","no"):
        print("Comando não identificado... tente novamente")
        continuar = input("Deseja descobrir se outro ano é bissexto?")

#Caso o usuário não queira identificar outro ano, o programa encerra.
print("PROGRAMA FINALIZADO....")
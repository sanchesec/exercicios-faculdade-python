print(" Identifique seu conceito sobre a média escolar...")

media = int(input("Insira sua média escolar (1-10) "))

if media >= 9:
    print("Conceito A")

elif media >= 7 and media < 9:
    print("Conceito B")

elif media >=5 and media <7:
    print("Conceito C")

else:
    print("Conceito D, melhore!")
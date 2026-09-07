#Escreva a função soma(a, b) que retorne a soma de dois números e imprima o resultado

Numberone = float(input("Insert a number: ").strip())
Numbertwo = float(input("Insert again a number: ").strip())

def soma(a,b):
    result = (a + b)
    return result

print(soma(Numberone,Numbertwo))
   
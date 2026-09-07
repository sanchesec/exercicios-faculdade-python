#Crie a função min_max(lista) que retorne o menor e o maior valor de uma lista (dois retornos)

def min_max(list):
    highnumber = max(list)
    lownumber = min(list)
    result = print(f"your high number is {highnumber} and you low number is {lownumber}")
    return result
    

insertother = "y"
listnumber = []

while insertother in ("y","yes"):

    num = int(input("Insert a number: ").strip())
    listnumber.append(num)
    insertother = input("You want insert other number?: ")
print(f"Your list is {listnumber}")
print(min_max(listnumber))




#Use um for para percorrer uma lista de nomes e imprimir 'Olá, <nome>!' para cada um
c = "y"
name = []

while c in ("y","yes"):
    newname = input("Insert name: ")
    name.append(newname)
    c = input("you want insert other?: ").strip().lower()

for n in name:
    print(f"Hello, {n}")
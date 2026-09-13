# Troque o item da posição 1 de uma lista por um novo valor e imprima a lista resultante.
list = ["Apple","Orange","Coconuts","Limon"]
print(f"Hello, at the moment your shopping cart is: {list} \n")
print(f"But... i feel that the item two ({list[1]}), is not the correct)\n")
itemcorrect = input("What the correct item?: ").strip()
list[1] = itemcorrect
print(f"Yeah!... now your shopping cart is {list}")


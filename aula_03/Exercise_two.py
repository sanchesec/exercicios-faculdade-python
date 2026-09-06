print("Let's get know each other")

name = input("What is your name?:").strip()
old = int(input(f"{name}?, that name cool, and what old are you?: ").strip())
heigth = input("And for last... whats is your height?: ").strip()
heigth = heigth.replace(",",".")
heigth = float(heigth)
print(f"Nice to meet you {name}, i know that you has {old} years and {heigth} at heigth")

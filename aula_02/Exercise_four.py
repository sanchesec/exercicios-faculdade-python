#4. Aplique a Lei de De Morgan para reescrever: not(idade >= 18 and tem_cnh)
old = int(input("Enter your age: "))
havecnh = input("You have CNH?: ").strip()

if havecnh in ("y","yes"):
    havecnh = True
else:
    havecnh = False

if not(old >= 18) or not(havecnh):
    print("Sorry, you do not have permission for drive")
else: print("You have permission for drive")
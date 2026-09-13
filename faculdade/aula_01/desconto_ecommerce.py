#Inicio programa
print("Verifique se você tem desconto...")

#Variáveis
valor_compra = float(input("Qual o valor da compra?: R$"))

vip = input("Você é um cliente vip?: ").strip().lower()

#Condições para desconto (Valor de compra maior que R$200 ou cliente ser VIP)
if valor_compra > 200 or vip in ("s,sim,ss"):
    print("Você recebeu um desconto de 10%...")
    print(f"De R${valor_compra} para R${(valor_compra)-(valor_compra * 0.1) }")

else:
    print("Desconto não aplicado..")
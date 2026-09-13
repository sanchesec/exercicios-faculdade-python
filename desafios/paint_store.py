print("Orçamento loja de tintas")
print("------------------------\n")

#var = [tipo,rendimento por m²,preço, litros de tinta, area que o usuario precisa pintar]
lata = ["Lata(s)",108,80,18]
galao = ["Galão(es)",21.6,25,3.6]

m = input("Insira o tamanho da área a ser pintada em M²: ").strip()
m = m.replace(",",".")
m = float(m)
m = m * 1.10

lata.append(m)
galao.append(m)

import math

quantlata = math.ceil(lata[4] / lata[1])
quantgalao = math.ceil(galao[4] / galao[1])
quantreslata = round(float((lata[3] * ((quantlata * lata[1]) - m)) / lata[1]), 2)
quantresgalao = round(float((galao[3] * ((quantgalao * galao[1]) - m)) / galao[1]), 2)

print("Você tem 3 opções de orçamento para compra da tinta\n")

print(f"Opção 1 - Comprar {quantlata} {lata[0]}, e pagar R${quantlata * lata[2]}, sobrando {quantreslata} litros de tinta")
print(f"Opção 2 - Comprar {quantgalao} {galao[0]}, e pagar R${quantgalao * galao[2]}, sobrando {quantresgalao} litros de tinta ")

vezeslata = m // lata[1]
rendmix = lata[1] * vezeslata
vezesgalao = math.ceil((m - rendmix) / galao[1])
rendmix += + (galao[1] * vezesgalao)
rendmix = rendmix - m
rendmix = round(rendmix/6,2)


print(f"Opção 3 - Comprar {vezeslata} {lata[0]} e {vezesgalao} {galao[0]}, pagando R${(vezeslata * lata[2]) + (vezesgalao * galao [2])}, sobrando {rendmix} litos ")

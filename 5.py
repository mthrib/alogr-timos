#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
maca = int(input("Quantas unidades vão ser compradas? "))

if maca < 12:
   valor_final1 = maca * 1.30
   print("Valor final = R$", valor_final1)
else:
    valor_final2 = maca * 1
    print("Valor final = R$", valor_final2)

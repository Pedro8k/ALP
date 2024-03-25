x = float(input("Digite o valor da sua compra: "))
if x <= 1000:
    precofinal = x * 0.9
    print ("O valor da compra era", x, ", mas com desconto valor a ser pago será de", precofinal, ", saindo com 10% de desconto")
elif x <= 5000:
    precofinal = x * 0.8
    print ("O valor da compra era", x, ", mas com desconto valor a ser pago será de", precofinal, ", saindo com 20% de desconto")
else: precofinal = x * 0.7
print ("O valor da compra era", x, ", mas com desconto valor a ser pago será de", precofinal, ", saindo com 30% de desconto")

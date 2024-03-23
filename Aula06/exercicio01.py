vhrs = (float) (input("Diga o valor da sua hora: "))
total_horas = (int) (input("Diga a quantidades de horas trabalhadas no mes: "))

salbruto = vhrs * total_horas

 #calculo do imposto de renda
if salbruto <= 900:
    ir = 0
    aliquota = 0
elif salbruto <= 1500:
    ir = salbruto * 0.05
    aliquota = 5
elif salbruto <= 2500:
    ir = salbruto * 0.1
    aliquota = 10
else:
    salbruto * 0.2
    aliquota = 20

inss = salbruto* 0.1

fgts = salbruto * 0.11

ims = salbruto * 0.03

totaldes = ir + inss

saliquido = salbruto - totaldes

print("Salario bruto: (", vhrs, "*", total_horas, ") : R$ ", salbruto)
print("(-) IR (",aliquota, "%) : R$ ", ir)
print("(-) INSS (10%) : R$ ", inss)
print("(-) FGTS (11%) : R$ ", fgts)
print("Total de descontos : R$ ", totaldes)
print("Salario liquido : R$ ", saliquido)






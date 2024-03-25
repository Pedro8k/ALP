x = float(input("Digite a largura de sua parede: "))
y = float(input("Digite a comprimento de sua parede: "))
paradesA = (x * 2.80) * 2
paradesB = (y * 2.80) * 2
porta = 0.80 * 2.10
totaldeparedes = paradesA + paradesB
totaldelitros = (totaldeparedes - porta) / 3
if (totaldelitros % 1) != 0:
   int (totaldelitros + 1)
   print("O total de latas que sera utilizado sera", int(totaldelitros),)
else:print("O total de latas que sera utilizado sera", int(totaldelitros),)

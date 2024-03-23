num = int(input("Me diga algum numero entre 0 a 999: "))

cent =int (num / 100)

dez =int ((num - cent * 100) / 10)

uni = int (((num - cent * 100) - dez * 10) / 1)

print(num, "= ", cent, "Centenas", ",", dez, "dezenas", "e", uni, "unidades")


a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado c: "))
if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
    print("Isso realmente é um triangulo")
    if (a == b) and (a == c) and (b == c):
        print("Isso realmente é um triangulo equilatero")
    elif (a == b) or (a == c) or (b == c):
        print("Isso realmente é um triangulo isosceles")
    else:
        print("Isso realmente é um triangulo escaleno")
else:
    print("Isso nem é um triangulo")
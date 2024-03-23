x = (float)(input("Me diga a sua nota: "))
y = (float)(input("Me diga a sua segunda nota: "))

media = (x + y) / 2

print(" Media de aproveitamento       Conceito")
print(" Entre 9.0 e 10.0                  A")
print(" Entre 7.5 e 9.0                   B")
print(" Entre 6.0 e 7.5                   C")
print(" Entre 4.0 e 6.0                   D")
print(" Entre 4.0 e 0.0                   E")

if media >= 9.0 :
    print("Sua nota é A")
    print(" Voce foi Aprovado")
elif (media >= 7.5) :
    print("Sua nota é B")
    print(" Voce foi Aprovado")
elif (media >= 6.0) :
    print("Sua nota é C")
    print(" Voce foi Aprovado")
elif (media >= 4.0) :
    print("Sua nota é D")
    print(" Voce foi reprovado")
else:
    print("Sua nota é E")
    print(" Voce foi reprovado")









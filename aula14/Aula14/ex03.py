def criar_lista():
    entrada = input("Digite os elementos: ")
    lista = list(entrada)
    lista_numeros = [int(numero) for numero in lista]
    return lista_numeros
def somar_lista(lista):
    soma = sum(lista)
    return soma

def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

minha_lista = criar_lista()
soma = somar_lista(minha_lista)
print("Soma dos números na lista:", soma)
produto = multiplicar_lista(minha_lista)
print("Produto dos números na lista:", produto)

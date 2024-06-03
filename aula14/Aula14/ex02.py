def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_ate(numero):
    lista_primos = []
    numero_atual = 2
    while len(lista_primos) < numero:
        if eh_primo(numero_atual):
            lista_primos.append(numero_atual)
        numero_atual += 1
    return lista_primos

Y = 13
alvo_inteiro = Y * 2 + 5
numeros_primos = primos_ate(alvo_inteiro)
soma_dos_primos = sum(numeros_primos)

print(f"A lista dos {alvo_inteiro} primeiros números primos é {numeros_primos}, com tamanho {len(numeros_primos)} e"
      f" a soma dos valores é {soma_dos_primos}.")

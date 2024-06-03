def contar_patos_coelhos(total_cabecas, total_pes):
    total_coelhos = (total_pes - total_cabecas * 2) // 2
    total_patos = total_cabecas - total_coelhos
    return total_patos, total_coelhos

total_cabecas = 13
total_pes = total_cabecas * 3 + 3
patos, coelhos = contar_patos_coelhos(total_cabecas, total_pes)

print(f"Patos: {patos}")
print(f"Coelhos: {coelhos}")
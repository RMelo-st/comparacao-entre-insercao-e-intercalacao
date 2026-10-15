
def ordenacao_insercao(lista):
    numeros = lista.copy()
    comparacoes = 0

    for i in range(1, len(numeros)):
        atual = numeros[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if numeros[j] > atual:
                numeros[j + 1] = numeros[j]
                j -= 1
            else:
                break

        numeros[j + 1] = atual

    return numeros, comparacoes


def ordenacao_intercalacao(lista):
    if len(lista) <= 1:
        return lista.copy(), 0

    meio = len(lista) // 2

    esquerda, comp_esquerda = ordenacao_intercalacao(lista[:meio])
    direita, comp_direita = ordenacao_intercalacao(lista[meio:])

    resultado = []
    i = 0
    j = 0
    comparacoes = comp_esquerda + comp_direita

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1

        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado, comparacoes

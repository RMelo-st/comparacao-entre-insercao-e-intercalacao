
from ordenacao import ordenacao_insercao, ordenacao_intercalacao


def testar_algoritmo(nome, funcao):
    casos = [
        ([], []),
        ([5], [5]),
        ([3, 3, 3], [3, 3, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([5, 3, 4, 1], [1, 3, 4, 5]),
    ]

    for entrada, esperado in casos:
        resultado, comparacoes = funcao(entrada)

        assert resultado == esperado, (
            f"{nome}: entrada {entrada}, resultado {resultado}"
        )
        assert comparacoes >= 0

    print(f"{nome}: todos os testes passaram!")


testar_algoritmo("Inserção", ordenacao_insercao)
testar_algoritmo("Intercalação", ordenacao_intercalacao)

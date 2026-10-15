
import csv
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from ordenacao import ordenacao_insercao, ordenacao_intercalacao


TAMANHOS = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
REPETICOES = 10
EXECUCOES_POR_LOTE = 100

PASTA = Path(__file__).parent
ARQUIVO_CSV = PASTA / "dados.csv"
PASTA_GRAFICOS = PASTA / "graficos"


class NumeroContado:
    comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        NumeroContado.comparacoes += 1
        return self.valor < outro.valor


def medir_tempo(funcao, lista):
    inicio = time.perf_counter()

    for _ in range(EXECUCOES_POR_LOTE):
        funcao(lista)

    fim = time.perf_counter()

    return (fim - inicio) / EXECUCOES_POR_LOTE


def medir_sorted_comparacoes(lista):
    NumeroContado.comparacoes = 0
    numeros = [NumeroContado(valor) for valor in lista]

    sorted(numeros)

    return NumeroContado.comparacoes


def executar_medicoes():
    resultados = []

    for tamanho in TAMANHOS:
        tempos_insercao = []
        tempos_intercalacao = []
        tempos_sorted = []
        comparacoes_insercao = []
        comparacoes_intercalacao = []
        comparacoes_sorted = []

        for _ in range(REPETICOES):
            lista = [random.randint(0, 10000) for _ in range(tamanho)]

            tempos_insercao.append(
                medir_tempo(ordenacao_insercao, lista)
            )
            tempos_intercalacao.append(
                medir_tempo(ordenacao_intercalacao, lista)
            )
            tempos_sorted.append(
                medir_tempo(sorted, lista)
            )

            _, comp = ordenacao_insercao(lista)
            comparacoes_insercao.append(comp)

            _, comp = ordenacao_intercalacao(lista)
            comparacoes_intercalacao.append(comp)

            comparacoes_sorted.append(
                medir_sorted_comparacoes(lista)
            )

        resultado = {
            "n": tamanho,
            "tempo_insercao": sum(tempos_insercao) / REPETICOES,
            "tempo_intercalacao": sum(tempos_intercalacao) / REPETICOES,
            "tempo_sorted": sum(tempos_sorted) / REPETICOES,
            "comparacoes_insercao": (
                sum(comparacoes_insercao) / REPETICOES
            ),
            "comparacoes_intercalacao": (
                sum(comparacoes_intercalacao) / REPETICOES
            ),
            "comparacoes_sorted": (
                sum(comparacoes_sorted) / REPETICOES
            ),
        }

        resultados.append(resultado)
        print(f"Concluído: n = {tamanho}")

    return resultados


def salvar_csv(resultados):
    campos = list(resultados[0].keys())

    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

    print(f"\nCSV salvo em: {ARQUIVO_CSV}")



def gerar_graficos(resultados):
    PASTA_GRAFICOS.mkdir(exist_ok=True)

    tamanhos = [r["n"] for r in resultados]

    # Grafico de tempo
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        tamanhos,
        [r["tempo_insercao"] for r in resultados],
        marker="o",
        label="Insercao"
    )
    ax.plot(
        tamanhos,
        [r["tempo_intercalacao"] for r in resultados],
        marker="s",
        label="Intercalacao"
    )
    ax.plot(
        tamanhos,
        [r["tempo_sorted"] for r in resultados],
        marker="^",
        label="sorted()"
    )

    ax.set_title("Comparacao do tempo de ordenacao")
    ax.set_xlabel("Tamanho da lista (n)")
    ax.set_ylabel("Tempo medio por execucao (segundos)")
    ax.set_yscale("log")
    ax.set_xticks(tamanhos)
    ax.tick_params(axis="x", labelrotation=45, labelsize=9)
    ax.legend()
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(PASTA_GRAFICOS / "tempos.png", dpi=200)
    plt.close(fig)

    # Grafico de comparacoes
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        tamanhos,
        [r["comparacoes_insercao"] for r in resultados],
        marker="o",
        label="Insercao"
    )
    ax.plot(
        tamanhos,
        [r["comparacoes_intercalacao"] for r in resultados],
        marker="s",
        label="Intercalacao"
    )
    ax.plot(
        tamanhos,
        [r["comparacoes_sorted"] for r in resultados],
        marker="^",
        label="sorted()"
    )

    ax.set_title("Comparacao do numero de comparacoes")
    ax.set_xlabel("Tamanho da lista (n)")
    ax.set_ylabel("Media de comparacoes")
    ax.set_yscale("log")
    ax.set_xticks(tamanhos)
    ax.tick_params(axis="x", labelrotation=45, labelsize=9)
    ax.legend()
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    fig.tight_layout()
    fig.savefig(PASTA_GRAFICOS / "comparacoes.png", dpi=200)
    plt.close(fig)

    print("Graficos salvos na pasta graficos.")

def main():
    print("Iniciando as medições...\n")

    resultados = executar_medicoes()
    salvar_csv(resultados)
    gerar_graficos(resultados)

    print("\nExperimento concluído.")


if __name__ == "__main__":
    main()

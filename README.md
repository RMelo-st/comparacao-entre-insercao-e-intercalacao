# Comparação entre Inserção e Intercalação

Projeto desenvolvido para comparar os algoritmos Insertion Sort e Merge Sort, analisando o tempo de execução e o número de comparações em listas de diferentes tamanhos.

O projeto também mede o tempo do `sorted()` do Python e conta suas comparações como atividade extra.

## Requisitos

- Python 3.12 ou compatível
- Matplotlib

## Como executar

### 1. Instalar a biblioteca

```bash
python -m pip install matplotlib
```

### 2. Executar os testes

```bash
python testes.py
```

Os testes verificam listas vazias, listas com um elemento, elementos repetidos, listas ordenadas, listas invertidas e uma lista desordenada.

### 3. Executar as medições

```bash
python medir.py
```

O programa executa as medições, calcula as médias e gera novamente os arquivos de resultados.

## Arquivos do projeto

- `ordenacao.py`: implementa os algoritmos de ordenação e a contagem de comparações.
- `testes.py`: verifica se os algoritmos ordenam corretamente.
- `medir.py`: executa os experimentos e gera o CSV e os gráficos.
- `dados.csv`: armazena as médias das medições.
- `graficos/tempos.png`: apresenta os tempos médios de execução.
- `graficos/comparacoes.png`: apresenta as médias de comparações.
- `RELATORIO.md`: contém as tabelas, os gráficos e a análise dos resultados.

## Observação

Os tempos podem variar conforme o computador, a carga do sistema operacional e as condições de execução. Para comparar os algoritmos, foram utilizadas listas aleatórias e múltiplas repetições.
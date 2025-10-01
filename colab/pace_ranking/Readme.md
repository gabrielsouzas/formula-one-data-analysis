# 🏎️ Análise e Ranking de Ritmo (Pace) de Pilotos da F1

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vWPcTWkd4UFBmfbzxxQ7wiA-m6AUly56)

## 💻 Visão Geral do Projeto

Este projeto é um notebook de análise de dados interativo que utiliza a biblioteca **FastF1** para buscar dados de sessões oficiais da Fórmula 1 (Corrida, Classificação, Treino Livre) e gerar um **Boxplot** detalhado do ritmo dos pilotos.

O objetivo principal é visualizar a **distribuição de tempos de volta rápida (quicklaps)** de cada piloto em uma sessão específica, permitindo identificar:

1.  O **ranking de ritmo** (pace) ordenado pela média dos tempos de volta.
2.  A **consistência** de cada piloto (através da dispersão do boxplot).
3.  A diferença de tempo para o piloto mais rápido.

## 🛠️ Tecnologias e Bibliotecas

O projeto foi desenvolvido em Python, rodando no ambiente Google Colab, e utiliza as seguintes bibliotecas:

- **`fastf1`**: Biblioteca principal para acesso e manipulação dos dados de telemetria e resultados da Fórmula 1.
- **`seaborn` e `matplotlib`**: Utilizadas para a visualização, gerando um boxplot customizado com cores oficiais de cada piloto.
- **`pandas`**: Para manipulação e pré-processamento dos dados de voltas (Laps).

## 🚀 Como Acessar e Executar

Este projeto é um notebook do Google Colab e pode ser executado diretamente no seu navegador.

1.  **Clique no badge "Open In Colab"** no topo deste README ou [neste link direto](https://colab.research.google.com/drive/1vWPcTWkd4UFBmfbzxxQ7wiA-m6AUly56).
2.  **Defina os Parâmetros:** Na seção **"Configuração dos dados da sessão"**, você pode alterar:
    - `year` (Ano, e.g., `2024`)
    - `gp` (Nome do Grande Prêmio, e.g., `"Singapore"`)
    - `session_type` (Tipo de sessão: `"Race"`, `"Qualifying"`, `"FP1"`, etc.)
3.  **Execute as Células:** No Colab, vá ao menu _Ambiente de execução_ e clique em _Executar tudo_. O notebook irá buscar os dados da F1, realizar os cálculos e exibir o gráfico.

## 📊 Estrutura e Análise

O notebook executa os seguintes passos:

1.  **Instalação/Configuração:** Instala o `fastf1` e configura o cache.
2.  **Busca de Dados:** Carrega os dados da sessão F1 especificada.
3.  **Filtragem:** Seleciona apenas as voltas rápidas (`pick_quicklaps()`), descartando voltas de entrada/saída de box.
4.  **Cálculo do Pace:** Calcula a **média (ou mediana)** do tempo de volta de cada piloto para determinar o ranking.
5.  **Visualização:** Cria um **Boxplot** onde:
    - Cada caixa representa a distribuição dos tempos de volta de um piloto.
    - A linha tracejada preta indica a **média de tempo de volta**.
    - O ranking é apresentado da **esquerda (mais rápido)** para a **direita (mais lento)**.
    - A diferença de tempo (`+X.XXXs`) para o piloto mais rápido é mostrada abaixo do gráfico.

## 💡 Resultados Esperados

O gráfico gerado permite uma análise rápida:

- **Ranking:** O piloto na extrema esquerda é o que teve o melhor ritmo médio na sessão.
- **Consistência:** Caixas (boxes) mais curtas e estreitas indicam que o piloto foi mais consistente em seus tempos de volta. Caixas longas sugerem maior variação (inconsistência).

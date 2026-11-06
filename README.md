# 📊 Análise de Atendimentos de TI (ETL em Python & Dashboard Power BI)

## 📌 Sobre o Projeto

Este projeto consiste na extração, tratamento, transformação e visualização de dados referentes aos atendimentos efetuados por uma equipe de Tecnologia da Informação (TI).

A partir de um banco de dados bruto consolidado em formato `.csv` (`banco_atendimentos_ti_consolidado.csv`), é executado um script automatizado em **Python** utilizando a biblioteca **Pandas**. O script limpa os registros, realiza conversões temporais, calcula o Tempo Médio de Atendimento (TMA) e gera visões agregadas dos chamados. Os resultados são exportados em uma planilha estruturada em formato `.xlsx` (`analise_atendimentos.xlsx`) para alimentar um **Dashboard interativo no Power BI** (`Dashboard_analise_atendimentos.pbix`).

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.x
* **Manipulação e Análise de Dados:** Pandas
* **Exportação de Planilhas:** OpenPyXL
* **Business Intelligence / Data Viz:** Power BI Desktop

---

## 🔄 Fluxo de Trabalho (Pipeline de Dados)

```
┌──────────────────────────────────────┐
│  banco_atendimentos_ti_consolidado.csv │ (Base Bruta)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          analise_dados.py            │ (Script de ETL e Tratamento em Python)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       analise_atendimentos.xlsx      │ (Planilha Multi-aba com Dados Agregados)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Dashboard_analise_atendimentos.pbix │ (Relatório Interativo no Power BI)
└──────────────────────────────────────┘
```

1. **Extração:** Leitura do arquivo CSV contendo os registros de chamados, datas de abertura/fechamento, técnicos, departamentos e categorias.
2. **Transformação (Python):**
   * Conversão das colunas de data para o tipo `datetime`.
   * Cálculo da duração dos chamados resolvidos em horas para determinar o Tempo Médio de Atendimento (TMA).
   * Agrupamento e contagem de atendimentos por mês, técnico, categoria e setor (departamento).
   * Cálculo da média diária geral de atendimentos.
3. **Carga:** Gravação dos DataFrames resultantes em abas separadas dentro do arquivo Excel `analise_atendimentos.xlsx`.
4. **Visualização:** Conexão do Power BI com o arquivo Excel para exibição de indicadores estratégicos e gráficos interativos.

---

## 📁 Estrutura do Repositório

```
.
├── banco_atendimentos_ti_consolidado.csv  # Base bruta de chamados de TI
├── banco_atendimentos_ti_consolidado.xlsx # Base bruta convertida
├── analise_dados.py                        # Script Python responsável pelo ETL
├── analise_atendimentos.xlsx              # Arquivo gerado pelo Python com visões agregadas
├── Dashboard_analise_atendimentos.pbix     # Relatório interativo do Power BI
└── README.md                               # Documentação do projeto
```

---

## 📄 Estrutura do Arquivo Gerado (`analise_atendimentos.xlsx`)

O script Python exporta automaticamente as seguintes abas para o Excel:

| Nome da Aba | Descrição dos Dados |
| :--- | :--- |
| `Atendimento_Setor` | Total de chamados abertos por departamento. |
| `Media_Diaria` | Média geral de atendimentos realizados por dia. |
| `TMA_Mensal` | Tempo Médio de Atendimento (em horas) agrupado por mês/ano. |
| `Atendimento_Tecnico` | Quantidade de chamados atendidos por cada técnico e especialidade. |
| `Atendimento_Tipo` | Distribuição do volume de chamados por categoria. |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Biblioteca `pandas` e `openpyxl`.
* Power BI Desktop.

### Execução do Script Python

1. Clone o repositório ou baixe os arquivos no mesmo diretório.
2. Certifique-se de que as dependências estejam instaladas:
   ```bash
   pip install pandas openpyxl
   ```
3. Execute o script de tratamento de dados:
   ```bash
   python analise_dados.py
   ```
4. O script exibirá a mensagem `"Dados tratados e exportados com sucesso para o arquivo Excel!"` e atualizará o arquivo `analise_atendimentos.xlsx`.

### Visualização no Power BI

1. Abra o arquivo `Dashboard_analise_atendimentos.pbix` no Power BI Desktop.
2. Caso o caminho do arquivo de origem mude, vá em **Transformar Dados > Configurações da Fonte de Dados** e atualize para o caminho local do seu `analise_atendimentos.xlsx`.
3. Clique em **Atualizar** na guia Página Inicial para carregar os novos dados calculados.

---

### 🖥️ Dashboard Interativa

<img width="861" height="488" alt="Sem título" src="https://github.com/user-attachments/assets/299d52cd-15bc-44da-b842-70ab5119de24" />


## ✉️ Contato

Desenvolvido por **Gabriel Cruz**  
* **LinkedIn:** (https://www.linkedin.com/in/gabriel-cruz-2935b719b/) 
* **GitHub:** (https://github.com/GabrielCDL)

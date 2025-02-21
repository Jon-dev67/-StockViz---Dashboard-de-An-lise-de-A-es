# Análise de Dados Financeiros com Python

Este projeto realiza uma análise de dados financeiros da ação da Apple (AAPL) utilizando dados históricos obtidos via Yahoo Finance. O objetivo é analisar o comportamento de preços, calcular indicadores financeiros e realizar simulações de portfólios de investimentos.

Além disso, um **dashboard interativo** foi criado utilizando **Streamlit**, permitindo uma visualização interativa dos dados e resultados da análise.

## Requisitos

Para rodar este projeto, é necessário ter instalado:

- Python 3.x
- Bibliotecas Python:
  - yfinance
  - seaborn
  - pandas
  - matplotlib
  - numpy
  - streamlit

Você pode instalar as dependências utilizando o seguinte comando:

```bash
pip install yfinance seaborn pandas matplotlib numpy streamlit

Descrição

O código realiza diversas análises e visualizações para ajudar na compreensão do desempenho da ação AAPL e outras ações selecionadas. As principais tarefas realizadas incluem:

Download de dados financeiros: Utilizando a API do Yahoo Finance (yfinance), os dados são baixados para um período de tempo específico.

Cálculo de indicadores técnicos:

Médias móveis de 20 e 50 dias.

Média Móvel Exponencial (EMA).

Índice de Força Relativa (RSI).

Retorno diário e retorno acumulado.


Análise de distribuição:

Histograma dos retornos diários.


Correlação entre múltiplas ações:

Análise de correlação entre os retornos diários de diferentes ações (AAPL, MSFT, GOOGL, AMZN).


Simulação de Portfólio:

Cálculo do retorno esperado e risco (volatilidade) de um portfólio com múltiplas ações.

Simulação de vários portfólios para encontrar a fronteira eficiente e o melhor portfólio baseado no índice de Sharpe.


Dashboard Interativo com Streamlit:

Visualização interativa de gráficos e resultados de indicadores financeiros.

Permite ao usuário escolher diferentes ações e visualizar gráficos de preço, médias móveis, retorno acumulado, RSI, e muito mais.



Como Usar

1. Clone o repositório:

git clone https://github.com/seu_usuario/projeto-analise-financeira.git
cd projeto-analise-financeira

2. Instale as dependências:

pip install -r requirements.txt

3. Execute o aplicativo Streamlit:

Para rodar o aplicativo Streamlit e ver as visualizações interativas, utilize o seguinte comando:

streamlit run app.py

O Streamlit abrirá automaticamente um servidor local e você poderá visualizar o aplicativo no navegador.

4. Execute o script em Python (opcional):

Caso queira rodar as análises sem o app, basta executar o script Python para gerar os gráficos e visualizar os resultados:

python analise_financeira.py

Exemplos de Saídas

Gráfico da Evolução do Preço da AAPL



Gráfico das Médias Móveis de 20 e 50 Dias



Gráfico do Retorno Acumulado da AAPL



Mapa de Calor da Correlação entre Ações



Simulação de Portfólio e Fronteira Eficiente



Resultados

O script também exibe o melhor portfólio baseado no Sharpe ratio, assim como o retorno esperado e o risco do portfólio.

Dashboard Streamlit

O dashboard interativo permite ao usuário:

Visualizar os gráficos de preços, médias móveis, e RSI de diferentes ações.

Interagir com os dados, permitindo uma análise mais dinâmica dos dados financeiros.


Conclusão

Este projeto fornece uma maneira prática de realizar análise financeira e simulação de portfólios utilizando dados históricos de ações. O Streamlit oferece uma interface simples e interativa para visualizar essas análises, facilitando a exploração dos dados financeiros. É possível utilizar este código como base para análises mais complexas, incluindo backtesting e otimização de portfólios.

Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

### Alterações principais:
1. **Adição do Streamlit**: No README, agora inclui o uso do Streamlit, permitindo ao usuário rodar o app para interagir com gráficos e visualizar as análises.
2. **Instruções de uso do Streamlit**: Foi adicionado o comando `streamlit run app.py` para rodar o app interativo.
3. **Descrição das funcionalidades interativas**: O Streamlit permite visualização interativa dos gráficos e resultados.

**Estrutura do Projeto (exemplo)**:

projeto-analise-financeira/ │ ├── analise_financeira.py          # Script principal para análise ├── app.py                         # Arquivo do Streamlit ├── imagens/                       # Diretório para imagens de gráficos (caso use) ├── requirements.txt               # Arquivo de dependências ├── README.md                      # Este arquivo └── LICENSE                        # Licença do projeto

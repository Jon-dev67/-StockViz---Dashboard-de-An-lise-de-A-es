import time
import os
from pyngrok import ngrok
import os

# Fechar qualquer processo do Streamlit
os.system("pkill -9 streamlit")

# Fechar qualquer processo do ngrok
os.system("pkill -9 ngrok")

# Caminho para o arquivo Python do Streamlit
script = '/content/app.py'

# Código do Streamlit
app_code = """
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Função para baixar dados das ações
def baixar_dados(acoes, start, end):
    return yf.download(acoes, start=start, end=end)

# Configuração da página
st.set_page_config(page_title="Análise de Ações - Dashboard", layout="wide")
st.title("Análise de Ações e Otimização de Portfólio")

# Definir período
data_inicio = "2023-01-20"
data_fim = "2025-02-20"

# Baixar dados da AAPL
df = baixar_dados("AAPL", data_inicio, data_fim)

# Criar médias móveis
df["MM_20"] = df["Close"].rolling(window=20).mean()
df["MM_50"] = df["Close"].rolling(window=50).mean()

# Plotar os preços e médias móveis
st.subheader("Preço de Fechamento e Médias Móveis")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Close'], label="Preço de Fechamento", color='blue')
ax.plot(df['MM_20'], label="Média Móvel 20 dias", color='red', linestyle='dashed')
ax.plot(df['MM_50'], label="Média Móvel 50 dias", color='green', linestyle='dashed')
ax.set_xlabel("Data")
ax.set_ylabel("Preço (USD)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Calcular Retorno Diário e Acumulado
df["Retorno Diário"] = df["Close"].pct_change()
df["Retorno Acumulado"] = (1 + df["Retorno Diário"]).cumprod()

# Plotar Retorno Acumulado
st.subheader("Retorno Acumulado da AAPL")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Retorno Acumulado"], label="Retorno Acumulado", color="purple")
ax.set_xlabel("Data")
ax.set_ylabel("Retorno (%)")
ax.legend()
ax.grid()
st.pyplot(fig)

# Baixar os dados da AAPL
df = yf.download("AAPL", start="2023-01-20", end="2025-02-20")

# Calcular Retorno Diário
df["Retorno Diário"] = df["Close"].pct_change()

# Estatísticas básicas
print(df[["Close", "Retorno Diário"]].describe())

# Histograma dos Retornos Diários
plt.figure(figsize=(10,5))
sns.histplot(df["Retorno Diário"].dropna(), bins=50, kde=True, color="purple")
plt.title("Distribuição dos Retornos Diários da AAPL")
plt.xlabel("Retorno Diário")
plt.ylabel("Frequência")
plt.grid()
plt.show()

# Calcular RSI
delta = df["Close"].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
df["RSI"] = 100 - (100 / (1 + rs))

# Plotar RSI
st.subheader("RSI da AAPL")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["RSI"], label="RSI", color="green")
ax.axhline(70, linestyle="dashed", color="red")
ax.axhline(30, linestyle="dashed", color="blue")
ax.set_xlabel("Data")
ax.legend()
ax.grid()
st.pyplot(fig)

# Baixar dados de múltiplas ações
acoes = ["AAPL", "MSFT", "GOOGL", "AMZN"]
df_multi = baixar_dados(acoes, data_inicio, data_fim)["Close"]

# Calcular correlação entre retornos
df_retornos = df_multi.pct_change().dropna()
correlacao = df_retornos.corr()

# Plotar Heatmap de correlação
st.subheader("Correlação entre Retornos das Ações")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Otimização de Portfólio
pesos = np.array([0.25, 0.25, 0.25, 0.25])
retorno_esperado = np.sum(df_retornos.mean() * pesos) * 252
cov_matriz = df_retornos.cov() * 252
risco_portfolio = np.sqrt(np.dot(pesos.T, np.dot(cov_matriz, pesos)))

st.subheader("Otimização de Portfólio")
st.write(f"Retorno Esperado: {retorno_esperado:.2%}")
st.write(f"Risco (Volatilidade): {risco_portfolio:.2%}")

# Simulação de múltiplos portfólios
np.random.seed(42)
n_portfolios = 10000
resultados = np.zeros((3, n_portfolios))

for i in range(n_portfolios):
    pesos = np.random.random(len(acoes))
    pesos /= np.sum(pesos)
    retorno_portfolio = np.sum(df_retornos.mean() * pesos) * 252
    risco_portfolio = np.sqrt(np.dot(pesos.T, np.dot(cov_matriz, pesos)))
    resultados[0, i] = retorno_portfolio
    resultados[1, i] = risco_portfolio
    resultados[2, i] = resultados[0, i] / resultados[1, i]

portfolios = pd.DataFrame(resultados.T, columns=["Retorno", "Risco", "Sharpe"])
melhor_portfolio = portfolios.loc[portfolios["Sharpe"].idxmax()]

# Plotar Fronteira Eficiente
st.subheader("Fronteira Eficiente")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(portfolios["Risco"], portfolios["Retorno"], c=portfolios["Sharpe"], cmap="viridis", marker="o")
ax.set_xlabel("Risco (Volatilidade)")
ax.set_ylabel("Retorno Esperado")
ax.set_title("Otimização de Portfólio: Fronteira Eficiente")
plt.colorbar(ax.collections[0], label="Sharpe Ratio")
ax.scatter(melhor_portfolio["Risco"], melhor_portfolio["Retorno"], color="red", marker="*", s=200, label="Melhor Portfólio")
ax.legend()
ax.grid()
st.pyplot(fig)

# Exibir dados do Melhor Portfólio
st.write("Melhor Portfólio:")
st.write(f"Retorno: {melhor_portfolio['Retorno']:.2%}")
st.write(f"Risco: {melhor_portfolio['Risco']:.2%}")
st.write(f"Sharpe Ratio: {melhor_portfolio['Sharpe']:.2f}")
"""

# Criar o arquivo de script no Colab
with open(script, 'w') as f:
    f.write(app_code)

# Iniciar o Streamlit no segundo plano
os.system(f"streamlit run {script} --server.port 8501 &")
time.sleep(10)  # Esperar o Streamlit começar

# Conectar ao ngrok
public_url = ngrok.connect(8501).public_url
print(f"Acesse o Streamlit aqui: {public_url}")
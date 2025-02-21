import yfinance as yf
import seaborn as sns
import pandas as pd
import datetime
import matplotlib.pyplot as plt


# Definir período
start = "2023-01-20"
end = "2025-02-20"

# Baixar os dados da Apple (AAPL)
df = yf.download("AAPL", start=start, end=end)

# Exibir as primeiras linhas
display(df)
df.info()
print(df.isnull().sum())


plt.figure(figsize=(10,5))
plt.plot(df["Close"],label="preco de fechamento", color="blue")
plt.title("evolução do preço da AAPL")
plt.xlabel("Data")
plt.ylabel("Preço ($)")
plt.legend()
plt.grid()
plt.show()

# criando médias móveis de 20 e 50 dias

df["MM_20"] = df["Close"].rolling(window=(20)).mean()
df["MM_50"] = df["Close"].rolling(window=(50)).mean()

#plotando médias móveis com o preço

plt.figure(figsize=(15,8))
plt.plot(df["Close"],label="preço fechamento",color="blue")
plt.plot(df["MM_20"],label="Média móvel 20 dias",color="red",linestyle="dashed")
plt.plot(df["MM_50"],label="Média móvel 50 dias",color="green",linestyle="dashed")
plt.title("AAPL-Preço e médias móveis ")
plt.xlabel("Data")
plt.ylabel("Preço ($)")
plt.legend()
plt.grid()
plt.show()

# Calcular Retorno Diário (%)
df["Retorno Diário"] = df["Close"].pct_change()

# Calcular Retorno Acumulado (%)
df["Retorno Acumulado"] = (1 + df["Retorno Diário"]).cumprod()

# Plotar Retorno Acumulado
plt.figure(figsize=(10,5))
plt.plot(df["Retorno Acumulado"], label="Retorno Acumulado", color="purple")
plt.title("Retorno Acumulado da AAPL")
plt.xlabel("Data")
plt.ylabel("Retorno (%)")
plt.legend()
plt.grid()
plt.show()

# Calcular Média Móvel Exponencial (EMA)
df["EMA_20"] = df["Close"].ewm(span=20, adjust=False).mean()

# Calcular RSI (Índice de Força Relativa)
window = 14
delta = df["Close"].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
rs = gain / loss
df["RSI"] = 100 - (100 / (1 + rs))

# Plotar EMA e RSI
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Gráfico de Preço + EMA
ax[0].plot(df["Close"], label="Preço de Fechamento", color="blue")
ax[0].plot(df["EMA_20"], label="EMA 20 dias", color="orange", linestyle="dashed")
ax[0].set_title("Preço e EMA da AAPL")
ax[0].legend()
ax[0].grid()

# Gráfico do RSI
ax[1].plot(df["RSI"], label="RSI", color="green")
ax[1].axhline(70, linestyle="dashed", color="red")  # Nível de sobrecompra
ax[1].axhline(30, linestyle="dashed", color="blue") # Nível de sobrevenda
ax[1].set_title("RSI da AAPL")
ax[1].legend()
ax[1].grid()

plt.tight_layout()
plt.show()


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

# Lista de ações
acoes = ["AAPL", "MSFT", "GOOGL"]

# Baixar dados de múltiplas ações
df = yf.download(acoes, start="2023-01-20", end="2025-02-20")

# Verificar quais colunas foram baixadas
print(df.columns)

# Usar "Adj Close" se disponível, caso contrário usar "Close"
if "Adj Close" in df.columns:
    df = df["Adj Close"]
else:
    df = df["Close"]

# Calcular os retornos diários
retornos = df.pct_change()

# Criar matriz de correlação
correlacao = retornos.corr()

# Exibir matriz de correlação
print(correlacao)

# Plotar heatmap da correlação
plt.figure(figsize=(8,6))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlação entre Retornos das Ações")
plt.show()

# Lista de ações no portfólio
acoes = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Baixar dados de todas as ações
df = yf.download(acoes, start="2023-01-20", end="2025-02-20")

# Calcular retornos diários
retornos = df["Close"].pct_change().dropna()  # Utilizando apenas o 'Close' para calcular os retornos

# Definir pesos do portfólio (exemplo: 25% para cada ação)
pesos = np.array([0.25, 0.25, 0.25, 0.25])

# Calcular retorno esperado do portfólio
retorno_esperado = np.sum(retornos.mean() * pesos) * 252  # 252 dias úteis no ano

# Calcular risco do portfólio (desvio padrão anualizado)
cov_matriz = retornos.cov() * 252
risco_portfolio = np.sqrt(np.dot(pesos.T, np.dot(cov_matriz, pesos)))

# Exibir resultados
print(f"Retorno Esperado do Portfólio: {retorno_esperado:.2%}")
print(f"Risco (Volatilidade) do Portfólio: {risco_portfolio:.2%}")

# Lista de ações no portfólio
acoes = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Baixar dados de todas as ações
df = yf.download(acoes, start="2023-01-20", end="2025-02-20")

# Calcular retornos diários
retornos = df["Close"].pct_change().dropna()  # Utilizando apenas o 'Close' para calcular os retornos

# Simulação de múltiplos portfólios
np.random.seed(42)  # Garantir resultados consistentes
n_portfolios = 10000
resultados = np.zeros((3, n_portfolios))

for i in range(n_portfolios):
    pesos = np.random.random(len(acoes))  # Gerar pesos aleatórios
    pesos /= np.sum(pesos)  # Normalizar para que a soma seja 1

    # Calcular retorno e risco do portfólio
    retorno_portfolio = np.sum(retornos.mean() * pesos) * 252  # 252 dias úteis no ano
    cov_matriz = retornos.cov() * 252
    risco_portfolio = np.sqrt(np.dot(pesos.T, np.dot(cov_matriz, pesos)))

    # Armazenar resultados
    resultados[0, i] = retorno_portfolio
    resultados[1, i] = risco_portfolio
    resultados[2, i] = resultados[0, i] / resultados[1, i]  # Sharpe ratio

# Converter resultados em DataFrame
portfolios = pd.DataFrame(resultados.T, columns=["Retorno", "Risco", "Sharpe"])

# Melhor portfólio (máximo Sharpe ratio)
melhor_portfolio = portfolios.loc[portfolios["Sharpe"].idxmax()]

# Plotar os portfólios simulados
plt.figure(figsize=(10,6))
plt.scatter(portfolios["Risco"], portfolios["Retorno"], c=portfolios["Sharpe"], cmap="viridis", marker="o")
plt.title("Otimização de Portfólio: Fronteira Eficiente")
plt.xlabel("Risco (Volatilidade)")
plt.ylabel("Retorno Esperado")
plt.colorbar(label="Sharpe Ratio")

# Destacar o portfólio ótimo (máximo Sharpe)
plt.scatter(melhor_portfolio["Risco"], melhor_portfolio["Retorno"], color="red", marker="*", s=200, label="Melhor Portfólio")
plt.legend()
plt.grid()
plt.show()

# Exibir o melhor portfólio
print("Melhor Portfólio (Máximo Sharpe Ratio):")
print(f"Retorno: {melhor_portfolio['Retorno']:.2%}")
print(f"Risco: {melhor_portfolio['Risco']:.2%}")
print(f"Sharpe Ratio: {melhor_portfolio['Sharpe']:.2f}")



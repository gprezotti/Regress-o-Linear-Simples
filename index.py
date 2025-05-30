import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import os

load_dotenv()

# Dados: semanas e matrículas
# Ler o CSV
df = pd.read_csv('dados.csv')
semanas = df[['semana']].values  # 2D
matriculas = df['matriculas'].values  # 1D

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(semanas, matriculas, test_size=0.2, random_state=42)

# Modelos
modelos = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# Treinar, prever e calcular MSE
resultados = {}
for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    resultados[nome] = {"modelo": modelo, "mse": mse, "predicoes": pred}
    print(f"{nome} -> MSE: {mse}")

# Melhor modelo
melhor_nome, melhor_dados = min(resultados.items(), key=lambda x: x[1]['mse'])

meta = int(os.getenv("META"))

# Soma das três primeiras previsões
soma_prevista = np.sum(melhor_dados['predicoes'][:3])

# Atingimento da meta (%)
atingimento = (soma_prevista / meta) * 100

# Margem de erro média em pontos percentuais
erro_absoluto_medio = np.mean(np.abs(y_test - melhor_dados['predicoes']))
margem_erro_pp = (erro_absoluto_medio / meta) * 100  # em pontos percentuais

print(f"\nMelhor modelo: {melhor_nome} com MSE: {melhor_dados['mse']}")
print("Matrículas previstas pelo melhor modelo:", np.round(melhor_dados['predicoes'], 2))
print(f"\nAtingimento médio da meta: {atingimento:.2f}%")
print(f"Margem de erro: ±{margem_erro_pp:.2f} pontos percentuais")
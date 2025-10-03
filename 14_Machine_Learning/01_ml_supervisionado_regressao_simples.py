# --- MACHINE LEARNING SUPERVISIONADO (REGRESSÃO LINEAR) ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# --- Exemplo 1: Regressão Linear Simples (y = 2x) ---
print("--- 1. Regressão Linear Simples (y=2x) ---")
X_train_simple = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train_simple = tf.constant([[2.0], [4.0], [6.0], [8.0]])

model_simple = Sequential()
model_simple.add(Dense(units=1, input_shape=(1,)))
model_simple.compile(optimizer='sgd', loss='mean_squared_error')
model_simple.fit(X_train_simple, y_train_simple, epochs=1000, verbose=0)

X_new = tf.constant([[5.0]])
prediction = model_simple.predict(X_new)
print(f"Predição para X=5.0: {prediction[0][0]:.2f} (Esperado: 10.0)")

# --- Exemplo 2: Previsão de Vendas com TensorFlow e Scikit-learn ---
print("\n--- 2. Previsão de Vendas (TensorFlow + Pandas/Sklearn) ---")
# Criação de dados fictícios
np.random.seed(42)
meses = np.arange(1, 13)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])
dados = pd.DataFrame({'Mes': meses, 'Vendas': vendas})

# Preparação dos dados
X = dados[['Mes']]
y = dados['Vendas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalização (Necessária para redes neurais)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo de Regressão Neural
model_sales = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=8, activation='relu'),
    tf.keras.layers.Dense(units=1)
])
model_sales.compile(optimizer='adam', loss='mean_squared_error')
model_sales.fit(X_train_scaled, y_train, epochs=500, verbose=0)

# Previsão e Avaliação (Usando dados não escalados para MSE)
predictions = model_sales.predict(X_test_scaled)
erro_mse = mean_squared_error(y_test, predictions)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Previsão para o próximo mês (Mês 13)
proximo_mes_scaled = scaler.transform(np.array([[13]]))
previsao_proximo_mes = model_sales.predict(proximo_mes_scaled)[0, 0]
print(f'Previsão de Vendas para o Mês 13: {previsao_proximo_mes:.2f}')
# Nota: A visualização via plt.show() é omitida no script do GitHub.

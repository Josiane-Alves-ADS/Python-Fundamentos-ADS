# CÉLULA 1: Importação de Bibliotecas e Carregamento de Dados (Passo 1)
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Bibliotecas importadas e TensorFlow configurado.")

# Carregar conjunto de dados Iris (4 features, 3 classes)
iris = load_iris()
X = iris.data # Features (sepal/petal length/width)
y = iris.target # Target (0, 1, 2)

# Exibir a forma dos dados para inspeção
print(f"Formato dos dados de entrada (X): {X.shape}")
print(f"Formato dos rótulos (y): {y.shape}")

# CÉLULA 2: Pré-processamento dos Dados (Passo 2)

# 2.1 Dividir o conjunto de dados em treinamento e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Tamanho do conjunto de treinamento: {X_train.shape[0]} amostras")
print(f"Tamanho do conjunto de teste: {X_test.shape[0]} amostras")

# 2.2 Normalizar os dados (Padronização)
# A normalização é crucial para Redes Neurais.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Dados padronizados com sucesso (média=0, desvio padrão=1).")

# CÉLULA 3: Construção, Treinamento e Avaliação do Modelo (Passos 3, 4, 5)

# PASSO 3: Construir o Modelo de Rede Neural (TensorFlow/Keras)
# O modelo terá 4 entradas (features da Iris) e 3 saídas (classes da Iris: 0, 1, 2).
model = Sequential([
    # Camada de entrada/escondida: 10 neurônios, ativação ReLU
    Dense(units=10, activation='relu', input_shape=(X_train_scaled.shape[1],)), 
    # Camada de saída: 3 neurônios (uma para cada classe), ativação Softmax (para classificação multiclasse)
    Dense(units=3, activation='softmax')
])

# Compilação do modelo
# Optimizer: 'adam' (otimizador comum)
# Loss: 'sparse_categorical_crossentropy' (para targets inteiros de classificação multiclasse)
# Metrics: 'accuracy' (precisão)
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

print("Modelo TensorFlow construído e compilado com sucesso.")

# PASSO 4: Treinar o Modelo
print("\n--- INICIANDO TREINAMENTO ---")
history = model.fit(X_train_scaled, y_train, 
                    epochs=150, # Número de épocas de treinamento
                    batch_size=32, 
                    verbose=0) # verbose=0 para não exibir o progresso linha por linha

print("Treinamento concluído em 150 épocas.")

# PASSO 5: Avaliar o Modelo
print("\n--- AVALIAÇÃO DO MODELO ---")
loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Precisão do Modelo no Conjunto de Teste: {accuracy * 100:.2f}%")

# CÉLULA 4: Fazer Previsões (Passo 6)

# Dados de uma nova flor (simulação: 4 features)
# Exemplo 1: Flor parecida com a Setosa (classe 0 - sépala longa, pétala curta)
nova_flor_1 = [[5.1, 3.5, 1.4, 0.2]] 
# Exemplo 2: Flor parecida com a Virginica (classe 2 - todas as medidas longas)
nova_flor_2 = [[7.0, 3.2, 5.5, 2.0]]

# Pré-processar os novos dados usando o mesmo scaler
nova_flor_1_scaled = scaler.transform(nova_flor_1)
nova_flor_2_scaled = scaler.transform(nova_flor_2)

# Fazer a previsão (o output é uma probabilidade para cada classe: [prob_0, prob_1, prob_2])
previsoes_prob_1 = model.predict(nova_flor_1_scaled, verbose=0)
previsoes_prob_2 = model.predict(nova_flor_2_scaled, verbose=0)

# A classe prevista é o índice com a maior probabilidade (argmax)
classe_prevista_1 = tf.argmax(previsoes_prob_1, axis=1).numpy()[0]
classe_prevista_2 = tf.argmax(previsoes_prob_2, axis=1).numpy()[0]

# Mapear o índice da classe para o nome da espécie (para o relatório)
nomes_classes = iris.target_names

print("\n--- RESULTADO DAS PREVISÕES ---")
print(f"Flor de Teste 1 (Entrada: {nova_flor_1[0]}):")
print(f"  Probabilidades: {previsoes_prob_1[0]}")
print(f"  Classe Prevista: {classe_prevista_1} ({nomes_classes[classe_prevista_1]})")
print("-" * 20)
print(f"Flor de Teste 2 (Entrada: {nova_flor_2[0]}):")
print(f"  Probabilidades: {previsoes_prob_2[0]}")
print(f"  Classe Prevista: {classe_prevista_2} ({nomes_classes[classe_prevista_2]})")

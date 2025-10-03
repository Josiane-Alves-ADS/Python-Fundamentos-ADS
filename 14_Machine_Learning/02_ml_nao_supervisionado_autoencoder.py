# --- MACHINE LEARNING NÃO SUPERVISIONADO (AUTOENCODER) ---
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import numpy as np

print("--- 1. Autoencoder Simples para Compressão de Dados ---")

# Dados de exemplo (Entrada e Saída são as mesmas)
# O modelo tentará aprender a reconstruir X_unsupervised, mas através de um gargalo (unidades=1)
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]], dtype=tf.float32)

# Estrutura do Autoencoder:
# Input (2) -> Encoding Layer (1) -> Decoding Layer (2)
input_layer = Input(shape=(2,))
encoded = Dense(units=1, activation='relu', name='encoder_layer')(input_layer)
decoded = Dense(units=2, activation='relu', name='decoder_layer')(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento (tenta reconstruir a si mesmo)
print("Treinando Autoencoder (1000 epochs)...")
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

# Previsão: O resultado deve ser muito próximo da entrada original
prediction_unsupervised = autoencoder.predict(X_unsupervised)

print("\nDados Originais:")
print(X_unsupervised.numpy())
print("\nPredição (Reconstrução):")
print(prediction_unsupervised)

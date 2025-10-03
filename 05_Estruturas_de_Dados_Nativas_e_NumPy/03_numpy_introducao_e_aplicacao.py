# --- INTRODUÇÃO À BIBLIOTECA NUMPY (Arrays e Cálculos) ---
import numpy as np

# Crie um array NumPy
my_array = np.array([1, 2, 3, 4, 5])
print("Array original:")
print(my_array)

# Operações matemáticas vetorizadas
squared_array = my_array ** 2
sum_of_elements = np.sum(my_array)
print("\nArray ao quadrado:")
print(squared_array)
print("Soma dos elementos:", sum_of_elements)


# --- APLICAÇÃO COMBINADA (Sets, Dicionários e Arrays) ---

participantes = [
    {"nome": "Alice", "localizacao": "EUA", "afiliacao": "Universidade A", "interesses": ["Física", "Astronomia"]},
    {"nome": "Bob", "localizacao": "Brasil", "afiliacao": "Instituto B", "interesses": ["Biologia", "Astronomia"]},
    {"nome": "Charlie", "localizacao": "Índia", "afiliacao": "Instituto C", "interesses": ["Química", "Engenharia"]}
]

# 1. Uso de sets para regiões
regioes = set(participante["localizacao"] for participante in participantes)
print("\nRegiões dos participantes (Set):", regioes)

# 2. Uso de dicionário para afiliações
afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

print("Afiliações dos participantes (Dict):")
for afiliacao, nomes in afiliacoes.items():
    print(f" {afiliacao}: {', '.join(nomes)}")

# 3. Uso de NumPy para análise
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]
print("Área de interesse mais popular (NumPy):", area_mais_popular)

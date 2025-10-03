# --- OBJETOS DO TIPO SEQUÊNCIA (STRINGS, LISTAS E TUPLAS) ---

# 1. Strings (Sequência)
texto = "Explorando a diversidade de linguagens de programação com Python."
print(f"Tamanho do texto: {len(texto)}")
print(f"As 5 primeiras letras são: {texto[:5]}")

# 2. Listas e List Comprehension
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
print("\n--- Listas e Iteração ---")
for p, cor in enumerate(cores):
    print(f'Posição = {p}, cor = {cor}')

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
linguagens_lower = [item.lower() for item in linguagens]
print(f"\nLista original: {linguagens[:3]}...")
print(f"Lista com List Comprehension: {linguagens_lower[:3]}...")


# 3. Funções de Ordem Superior (map e filter com lambda)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(f"\nPreços convertidos para R$: {precos_em_reais}")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares (Filter): {numeros_pares}")


# 4. Tuplas
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"\n--- Tuplas ---")
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

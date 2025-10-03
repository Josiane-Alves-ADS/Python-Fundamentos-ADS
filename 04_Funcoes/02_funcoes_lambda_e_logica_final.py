# --- FUNÇÕES ANÔNIMAS (LAMBDA) ---

# Função lambda para somar
soma_lambda = lambda a, b: a + b
resultado = soma_lambda(3, 4)
print(f"Resultado da soma lambda: {resultado}")


# --- APLICAÇÃO DE FUNÇÕES (MÉDIA E ARREDONDAMENTO) ---

# Lista de notas
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média (usa built-in sum e len)
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar situação (simulando um ternário Python)
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# Resultados
print("\n--- Resultados Finais ---")
print(f"Notas dos estudantes: {notas}")
print(f"Média calculada: {media_arredondada}")
print(f"Situação: {situacao}")

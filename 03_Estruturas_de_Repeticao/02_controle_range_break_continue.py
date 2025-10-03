# --- CONTROLE DE REPETIÇÃO: RANGE, BREAK E CONTINUE ---

# Método 1: Repetição por quantidade (0 a 4)
print("--- Método 1: range(5) ---")
for x in range(5):
    print(x)

print("-" * 10)

# Método 2: Limites inicial e superior (2 a 6)
print("--- Método 2: range(2, 7) ---")
for y in range(2, 7):
    print(y)

print("-" * 10)

# Método 3: Com incremento (1 a 10, pulando 2)
print("--- Método 3: range(1, 11, 2) ---")
for z in range(1, 11, 2):
    print(z)

# Demonstração do BREAK (para a execução do loop)
print("\n--- Demonstração do BREAK ---")
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"Número par encontrado: {numero}. Quebrando o loop.")
        break
    
# Demonstração do CONTINUE (pula a iteração atual)
print("\n--- Demonstração do CONTINUE ---")
for numero in range(1, 7):
    if numero == 5:
        print("Pulando a iteração 5 (continue).")
        continue
    print(numero)

# --- CLASSIFICAÇÃO DE FAIXA ETÁRIA COM ELIF ---

# Atribuição da variável (pode ser alterada para teste)
idade = 25

# Estrutura condicional aninhada (if/elif/else)
if idade < 18:
    print("Menor de idade")
elif idade < 65:  # Já sabemos que é >= 18
    print("Adulto")
else:
    print("Idoso")

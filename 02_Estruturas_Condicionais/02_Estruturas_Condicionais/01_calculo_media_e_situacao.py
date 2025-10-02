# --- CALCULADORA DE MÉDIA E SITUAÇÃO DO ALUNO ---

# Usamos int() para garantir que a entrada seja tratada como número inteiro para o cálculo.

print("--- Calculadora de Média e Situação do Aluno ---")
print("Digite a primeira nota:")
nota_1 = int(input())

print("Digite a segunda nota:")
nota_2 = int(input())

print("Digite a terceira nota:")
nota_3 = int(input())

print("Digite a quarta nota:")
nota_4 = int(input())

# Cálculo da média
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# --- ESTRUTURA CONDICIONAL (IF/ELSE) ---
if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

# Exibição do resultado
print(f"\nA média final é: {media}")
print(f"A situação do aluno é: {situacao}")

# --- OPERAÇÕES CRUD (CREATE, READ, UPDATE, DELETE) ---
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# --- CREATE (INSERÇÃO) ---
dados_exemplo = [
    ('Camiseta', 19.99, 50),
    ('Caneca', 12.50, 100),
    ('Mousepad', 8.90, 75)
]
cursor.executemany("INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)", dados_exemplo)
conn.commit()
print("Dados iniciais inseridos (CREATE).")


# --- READ (LEITURA) ---
cursor.execute("SELECT id, nome, preco FROM Produtos")
produtos = cursor.fetchall()
print("\n--- Produtos Atuais (READ) ---")
for produto in produtos:
    print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]:.2f}")


# --- UPDATE (ATUALIZAÇÃO) ---
novo_preco = 24.99
produto_id_update = 1 
cursor.execute("UPDATE Produtos SET preco = ? WHERE id = ?", (novo_preco, produto_id_update))
conn.commit()
print(f"\nProduto ID {produto_id_update} atualizado (UPDATE).")


# --- DELETE (EXCLUSÃO) ---
produto_id_delete = 2
cursor.execute("DELETE FROM Produtos WHERE id = ?", (produto_id_delete,))
conn.commit()
print(f"Produto ID {produto_id_delete} excluído (DELETE).")


# --- READ FINAL (VERIFICAÇÃO) ---
cursor.execute("SELECT id, nome FROM Produtos")
print("\n--- Produtos Restantes ---")
for produto in cursor.fetchall():
    print(produto)

# Fechando a conexão
conn.close()

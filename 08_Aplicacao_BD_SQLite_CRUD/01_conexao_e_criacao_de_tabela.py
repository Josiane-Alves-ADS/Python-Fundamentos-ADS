# --- CONEXÃO COM BANCO DE DADOS (SQLITE) E CRIAÇÃO DE TABELA ---
import sqlite3

# 1. Conectar ao banco de dados (o arquivo 'exemplo.db' será criado se não existir)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela Produtos
create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""
# 4. Executar o comando SQL
cursor.execute(create_table)

# 5. Confirmar as alterações (COMMIT) no banco de dados
conn.commit()

# 6. Fechar a conexão
conn.close()

print("Banco de dados 'exemplo.db' e tabela 'Produtos' criados com sucesso.")

# =================================================================
# ROTEIRO DE AULA PRÁTICA - MÓDULO 1: GESTÃO DE NOTAS DE ALUNOS
# =================================================================

# 1. Armazenamento das notas
# Uma lista vazia para guardar todas as notas inseridas pelo usuário.
notas_aluno = []

# =======================
# FUNÇÕES DO SISTEMA
# =======================

def adicionar_notas(lista_notas):
    """
    Função que permite ao usuário inserir notas.
    Utiliza um loop de repetição (while) para coletar múltiplas notas.
    """
    print("\n--- Cadastro de Notas ---")
    while True:
        # Estrutura condicional try-except para garantir que a entrada seja um número válido
        try:
            nota = input("Digite uma nota (ou 'fim' para terminar): ").strip().lower()
            
            if nota == 'fim':
                break
            
            valor_nota = float(nota)
            
            # Estrutura condicional para validar o intervalo da nota (opcional, mas boa prática)
            if 0 <= valor_nota <= 10:
                lista_notas.append(valor_nota)
                print(f"Nota {valor_nota} adicionada.")
            else:
                print("ERRO: A nota deve estar entre 0 e 10.")
        
        except ValueError:
            print("ERRO: Entrada inválida. Por favor, digite um número ou 'fim'.")
    
    # Estrutura condicional final: verifica se alguma nota foi adicionada
    if not lista_notas:
        print("Nenhuma nota foi registrada.")


def calcular_media(lista_notas):
    """
    Função que calcula a média aritmética das notas na lista.
    Retorna 0 se a lista estiver vazia para evitar erro de divisão por zero.
    """
    if not lista_notas:
        return 0
    # O comando sum() soma todos os elementos da lista.
    # O comando len() retorna o número total de elementos.
    media = sum(lista_notas) / len(lista_notas)
    return media


def determinar_situacao(media):
    """
    Função que utiliza estruturas condicionais para determinar a situação do aluno.
    """
    # Estrutura Condicional Principal
    if media >= 7.0:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
    
    return situacao


def exibir_relatorio(lista_notas, media, situacao):
    """
    Função para exibir o relatório final de forma organizada.
    """
    print("\n" + "="*40)
    print("      RELATÓRIO FINAL DO ALUNO")
    print("="*40)
    
    print(f"Notas Inseridas: {lista_notas}")
    print(f"Média Calculada: {media:.2f}")
    
    # Utiliza uma estrutura condicional no relatório para destacar o resultado
    if situacao == "APROVADO":
        print(f"SITUAÇÃO: {situacao} 🎉")
    else:
        print(f"SITUAÇÃO: {situacao} 😥")
        
    print("="*40)


# =======================
# FLUXO PRINCIPAL DO SISTEMA
# =======================

if __name__ == "__main__":
    
    # 1. Chama a função de cadastro para preencher a lista 'notas_aluno'
    adicionar_notas(notas_aluno)
    
    # Verifica se há notas para calcular antes de prosseguir
    if notas_aluno:
        # 2. Chama a função de cálculo
        media_final = calcular_media(notas_aluno)
        
        # 3. Chama a função de determinação da situação
        situacao_final = determinar_situacao(media_final)
        
        # 4. Chama a função de relatório
        exibir_relatorio(notas_aluno, media_final, situacao_final)
    else:
        print("\nProcesso encerrado. Não é possível gerar o relatório sem notas.")

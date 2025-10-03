# --- INTRODUÇÃO A TESTES COM PYTHON (ASSERT, DOCTEST, UNITTEST) ---

# A função central que será testada
def sum_numbers(numbers):
    """
    Soma os números em uma lista e contém os doctests.
    
    Exemplos (Doctests):
    >>> sum_numbers([1, 2, 3, 4])
    10
    >>> sum_numbers([-1, 0, 1])
    0
    >>> sum_numbers([])
    0
    """
    return sum(numbers)

# --- 1. Testes com ASSERT ---
def run_assert_tests():
    """Testes rápidos usando a palavra-chave assert."""
    print("--- 1. Testes com Assert (Verificações rápidas) ---")
    
    # Teste 1: Soma de positivos
    assert sum_numbers([1, 2, 3, 4]) == 10, "Erro: Assert falhou para números positivos"
    
    # Teste 2: Soma de mistos
    assert sum_numbers([-1, 0, 1]) == 0, "Erro: Assert falhou para números mistos"
    
    # Teste 3: Lista vazia
    assert sum_numbers([]) == 0, "Erro: Assert falhou para lista vazia"
    
    print("Todos os testes 'assert' foram concluídos com sucesso.")
    print(f"Exemplo de uso: sum_numbers([1, 2, 3, 5]) = {sum_numbers([1, 2, 3, 5])}")


# --- 2. Testes com DOCTEST ---
def run_doctests():
    """Executa os testes embutidos na docstring da função."""
    import doctest
    print("\n--- 2. Testes com Doctest (Na Documentação) ---")
    # O resultado será impresso no console: (failed=0, attempted=3)
    results = doctest.testmod(verbose=False)
    print(f"Resultado do Doctest: Tentativas={results.attempted}, Falhas={results.failed}")


# --- 3. Testes com UNITTEST ---
import unittest

class TestSumNumbers(unittest.TestCase):
    """Classe de testes unitários para a função sum_numbers."""
    
    def test_sum_numbers_positive(self):
        """Verifica se a soma de números positivos está correta."""
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)
        
    def test_sum_numbers_mixed(self):
        """Verifica se a soma de números mistos está correta."""
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)
        
    def test_sum_numbers_empty(self):
        """Verifica se a soma de uma lista vazia retorna zero."""
        self.assertEqual(sum_numbers([]), 0)

def run_unittests():
    """Executa o módulo unittest."""
    print("\n--- 3. Testes com Unittest (Framework Padrão) ---")
    # unittest.main() requer argumentos especiais para rodar dentro de um script ou IDE
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    
if __name__ == '__main__':
    run_assert_tests()
    run_doctests()
    run_unittests()

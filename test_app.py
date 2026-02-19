"""
Tests für die Beispiel-Anwendung
"""
import pytest
from app import add_numbers, multiply_numbers, divide_numbers, greet_user

class TestMathOperations:
    """Test-Klasse für mathematische Operationen"""
    
    def test_add_numbers(self):
        """Test für die Addition"""
        assert add_numbers(2, 3) == 5
        assert add_numbers(-1, 1) == 0
        assert add_numbers(0, 0) == 0
        assert add_numbers(10.5, 2.5) == 13.0
    
    def test_multiply_numbers(self):
        """Test für die Multiplikation"""
        assert multiply_numbers(2, 3) == 6
        assert multiply_numbers(-1, 5) == -5
        assert multiply_numbers(0, 10) == 0
        assert multiply_numbers(2.5, 4) == 10.0
    
    def test_divide_numbers(self):
        """Test für die Division"""
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(7, 2) == 3.5
        assert divide_numbers(-10, 2) == -5.0
        
    def test_divide_by_zero(self):
        """Test für Division durch Null"""
        with pytest.raises(ValueError, match="Division durch Null ist nicht erlaubt"):
            divide_numbers(10, 0)

class TestUserGreeting:
    """Test-Klasse für Benutzer-Begrüßung"""
    
    def test_greet_user_valid_name(self):
        """Test für gültige Namen"""
        assert greet_user("Alice") == "Hallo, Alice!"
        assert greet_user("Bob") == "Hallo, Bob!"
        assert greet_user("Jenkins") == "Hallo, Jenkins!"
    
    def test_greet_user_empty_name(self):
        """Test für leere Namen"""
        with pytest.raises(ValueError, match="Name muss ein nicht-leerer String sein"):
            greet_user("")
        
        with pytest.raises(ValueError, match="Name muss ein nicht-leerer String sein"):
            greet_user(None)
    
    def test_greet_user_invalid_type(self):
        """Test für ungültige Typen"""
        with pytest.raises(ValueError, match="Name muss ein nicht-leerer String sein"):
            greet_user(123)
        
        with pytest.raises(ValueError, match="Name muss ein nicht-leerer String sein"):
            greet_user(['Alice'])

def test_integration():
    """Integration-Test"""
    # Teste eine Kombination von Funktionen
    result1 = add_numbers(5, 3)
    result2 = multiply_numbers(result1, 2)
    final_result = divide_numbers(result2, 4)
    
    assert final_result == 4.0
    
    # Teste Begrüßung nach Berechnung
    greeting = greet_user("Tester")
    assert "Tester" in greeting
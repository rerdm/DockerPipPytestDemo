"""
Beispiel-Anwendung für die Jenkins Pipeline Demo
"""

def add_numbers(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

def multiply_numbers(a, b):
    """Multipliziert zwei Zahlen und gibt das Ergebnis zurück."""
    return a * b

def divide_numbers(a, b):
    """Teilt zwei Zahlen und gibt das Ergebnis zurück."""
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b

def greet_user(name):
    """Begrüßt einen Benutzer mit seinem Namen."""
    if not name or not isinstance(name, str):
        raise ValueError("Name muss ein nicht-leerer String sein")
    return f"Hallo, {name}!"

if __name__ == "__main__":
    print("Beispiel-Anwendung läuft...")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"4 * 5 = {multiply_numbers(4, 5)}")
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print(greet_user("Jenkins"))
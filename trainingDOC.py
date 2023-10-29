# Beispiel: Verwendung des Schlüsselworts "class"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hallo, ich bin {self.name}, {self.age} Jahre alt.")

# Instanziierung der Klasse Person
person1 = Person("Max", 25)

# Aufruf der Methode greet()
person1.greet()
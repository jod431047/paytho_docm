x = 10  # Eine globale Variable

def modify_global_variable():
    global x  # Deklaration, dass die Variable "x" global verwendet wird
    x = 20    # Änderung des Werts der globalen Variable "x"

print(x)  # Ausgabe: 10
modify_global_variable()
print(x)  # Ausgabe: 20
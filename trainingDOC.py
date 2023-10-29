def divide_numbers(a, b):
    try:
        result = a / b
        print("Ergebnis:", result)
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt.")
    finally:
        print("Das 'finally'-Block wird immer ausgeführt.")

divide_numbers(10, 2)
divide_numbers(8, 0)
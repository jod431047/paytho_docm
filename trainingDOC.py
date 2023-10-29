def calculate_factorial(n):
    if n < 0:
        raise ValueError("Die Fakultät ist nur für nicht-negative Zahlen definiert.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

try:
    number = int(input("Gib eine Zahl ein: "))
    result = calculate_factorial(number)
    print("Die Fakultät von", number, "ist", result)
except ValueError as e:
    print("Fehler:", e)
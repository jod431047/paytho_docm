def divide(a, b):
    assert b != 0, "Division durch Null ist nicht erlaubt!"
    return a / b

numerator = 10
denominator = 0

result = divide(numerator, denominator)
print(result)
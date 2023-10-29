try:
    # Code, der möglicherweise eine Ausnahme auslöst
    x = 10 / 0
except ZeroDivisionError:
    # Code, der ausgeführt wird, wenn eine ZeroDivisionError-Ausnahme auftritt
    print("Eine Division durch Null ist nicht erlaubt!")
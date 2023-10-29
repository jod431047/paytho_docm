def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 5
        print("Inner function: x =", x)

    inner_function()
    print("Outer function: x =", x)

outer_function()
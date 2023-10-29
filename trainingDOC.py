def generate_numbers():
    for i in range(1, 6):
        yield i

numbers = generate_numbers()

for num in numbers:
    print(num)
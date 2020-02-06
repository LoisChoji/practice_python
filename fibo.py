def fibonacci_numbers_at_index(count):
    if count <= 1:
        return count
    else:
        return fibonacci_numbers_at_index(count - 1) + fibonacci_numbers_at_index

count = 5
i = 1
while i<= count:
    print(fibonacci_numbers_at_index(i))
    i += 1
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

def square_of_sums(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total ** 2

print square_of_sums(100) - sum_of_squares(100)

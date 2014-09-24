def is_prime(n):
    prime = True
    for i in xrange(2, n - 1):
        if n % i == 0:
            prime = False
            break
    return prime

total = 0
for i in xrange(2, 11):
    if is_prime(i):
        total += i

print total

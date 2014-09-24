def is_prime(n):
    prime = True
    for i in xrange(2, n - 1):
        if n % i == 0:
            prime = False
            break
    return prime

def get_nth_prime(n):
    count = 0
    i = 2
    while True:
        if is_prime(i):
            count += 1
            i += 1
            if count == n:
                break
        else:
            i += 1
    return i - 1

print get_nth_prime(10001)

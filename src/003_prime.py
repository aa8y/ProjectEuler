def is_prime(n):
  prime = True
  for i in xrange(2, n - 1):
    if n % i == 0:
      prime = False
      break
  return prime

if __name__ == '__main__':
    n = 600851475143
    i = 2
    factor = 1

    while True:
        if n % i == 0:
            factor = n / i
            if is_prime(factor): 
                break
            else:
                i += 1
        else:
            i += 1
    print factor

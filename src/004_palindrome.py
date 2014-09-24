def is_palindrome(n):
    orig = str(n)
    rev = orig[::-1]
    if orig == rev:
        return True
    else:
        return False

if __name__ == '__main__':
    rev_100 = range(100, 1001)[::-1]

    for i in rev_100:
        for j in rev_100:
            mul = i * j
            if is_palindrome(mul):
                print mul
                break

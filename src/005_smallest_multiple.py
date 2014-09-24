def is_evenly_divisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

def get_largest_evenly_divisible(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num

num = get_largest_evenly_divisible(20)
for i in range (2, 21):
    tnum = num
    while is_evenly_divisible(tnum):
        num = tnum
        tnum /= i

print num

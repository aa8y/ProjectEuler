def is_pythagorean_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

def get_all_triplets(n):
    triplets = []
    for a in range(0, n + 1):
        print "%f" %(a / 10)
        for b in range(0, n + 1):
            for c in range(0, n + 1):
                if a < b and b < c:
                    if is_pythagorean_triplet(a, b, c):
                        triplets.append((a, b, c))
    return triplets

num = 1000
ptrips = get_all_triplets(num)
for ptrip in ptrips:
    #print ptrip
    if ptrip[0] + ptrip[1] + ptrip[2] == num:
        print ptrip

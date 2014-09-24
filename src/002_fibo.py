def gen_fibo(upto):
  pre = 0
  next = 1
  fibo = [0, 1]
  while True:
    inter = next
    next += pre
    pre = inter
    if next <= upto:
      fibo.append(next)
    else:
      break
  return fibo

def get_even_total(nums):
  total = 0
  for num in nums:
    if num % 2 == 0:
      total += num
  return total

f = gen_fibo(4000000)
print get_even_total(f)

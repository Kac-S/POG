def INT(x):
  for i in range(len(x)):
    x[i] = int(x[i])
  return x

def POWER(a, n):
  if n == 0:
    return 1
  if n % 2 == 1:
    return a * (POWER(a, (n - 1)/2))**2
  else:
    (POWER(a, n/2))**2
  return (POWER(a, n/2))**2
  
def FACT(n):
  c = []
  k = 2
  while n != 1:
    while n % k == 0:
      n //= k
      c.append(k)
    k += 1
  return c

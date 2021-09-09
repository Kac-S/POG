def INT(x):
  for i in range(len(x)):
    x[i] = int(x[i])
  return x

def ARRAY(l):
  a = [0]
  for i in range(1, l):
    a.append(0)
  return a

 # a = []*l

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

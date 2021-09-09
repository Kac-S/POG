import sys
import random

def POWER(a, n):
  if n == 0:
    return 1
  if n % 2 == 1:
    return a * (POWER(a, (n - 1)/2))**2
  else:
    (POWER(a, n/2))**2
  return (POWER(a, n/2))**2

GREEN = "\033[0;32m"

sys.stdout.write(GREEN)

while 1: print(random.randint(0, POWER(2137, 420)))
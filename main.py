dwajedentrzysiedem = [2,1,3,7,5]

x = 0
n = int(input())
for i in range(len(dwajedentrzysiedem)):
  if i > n - 1:
    break
  if dwajedentrzysiedem[i] > x:
    x = dwajedentrzysiedem[i]

print(x)


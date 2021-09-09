n = int(input())
x = list(reversed(list(map(int, input().split()))))
a = x[0] + 1
c = 0

for i in x:
    if i < a:
        a = i
    else:
        a -= 1
        c += 1

if a <= 0:
    print(-1)
else:
    print(c)


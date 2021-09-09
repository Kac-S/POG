import itertools
n = int(input())
lst = [list(i) for i in itertools.product([0, 1], repeat=n)]
for x in lst:    
    pr = ""
    for i in x:
        pr+=str(i)
    print(pr)

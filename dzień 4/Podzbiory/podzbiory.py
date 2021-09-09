<<<<<<< HEAD
import itertools
n = int(input())
lst = [list(i) for i in itertools.product([0, 1], repeat=n)]
for x in lst:    
    pr = ""
    for i in x:
        pr+=str(i)
    print(pr)
	
=======
>>>>>>> 67964fea3bf0b72eb9c1aa08db8a6649d7c720c3

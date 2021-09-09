import itertools
n = int(input())
lst = [list(i) for i in itertools.product([0, 1], repeat=n)]
lst = list(map(str, lst))
pr = ''
for x in lst:
	#x zamienić w stringa
	pr = pr + x +'\n'
print(pr)


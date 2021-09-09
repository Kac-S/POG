#przedstawiam nową wersję niesamowitego algorytmu, zdolną do zdobycia 3 punktów na 100 możliwych
# jeżeli go naprawisz, to jesteś bogolem, bo ja już nie potrafię
# P.S mamusiu ratuj

n, m = tuple(map(int, input().split()))
k = []
for x in range(n):
	k += list(map(int, input().split()))

kom = k[-1]
odw = []
energia = 1
while True:
	if kom == 1:
		print(energia)
		break
	elif kom in odw:
		print("NIE")
		break
	else:
		energia += 1
		odw.append(kom)
		kom = k[kom-1]
exit()






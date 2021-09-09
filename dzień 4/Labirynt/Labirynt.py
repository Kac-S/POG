#przedstawiam niesamowity algorytm, zdolny do zdobycia 1 punktu na 100 możliwych
# jeżeli go naprawisz, to jesteś bogolem, bo ja już nie potrafię
# P.S mamusiu ratuj
#n, m = tuple(map(int, input().split()))
#k = []
#for x in range(n):
#	k += list(map(int, input().split()))
n, m = 3, 4
k = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(k)
odw = [k[-1]]
nast = k[-1]
energia = 0

if nast == 1:
	print(1)
	exit()
while True:
	kom = k[nast-1]
	odw.append(kom)
	print("O", odw)
	if kom == 1:
		print(energia)
		break
		exit()
	elif kom in odw:
		print('NIE')
		break
		exit()
	else:
		nast = kom
	energia += 1






def main():

	print('\n----------TOWER OF HANOI---------\n\n')
	N=int(input('Enter the number of discs:'))
	print('\n')

	s='S'
	i='I'
	t='T'

	SolveHanoi(N,s,i,t)


def SolveHanoi(N,s,i,t):

	if N>1:
	
		SolveHanoi(N-1,s,t,i)

		print('Move disc ',N,' from peg',s,'to',t)

		SolveHanoi(N-1,i,s,t)


	elif N==1:

		print('Move disc ',N,' from peg',s,'to',t)

if __name__ == '__main__':
	main()


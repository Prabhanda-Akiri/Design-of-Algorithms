def main():

	n=int(input('Enter the number of intervals:	'))

	intv=[[] for i in range(n)]

	print('Enter the intervals:	\n')

	for i in range(n):
		s=input()
		s=s.split()
		intv[i].append(int(s[0]))
		intv[i].append(int(s[1]))

	#print(intv)
	intv.sort(key=lambda x : x[1])
	#print(intv)

	final_intv=[]
	prev_end=0

	while(intv):

		pres=intv.pop(0)
		if pres[0]>prev_end:
			final_intv.append(pres)
			prev_end=pres[1]

	print('\nThe subset of non-overlaping intervals are:	\n')

	for i in range(len(final_intv)):

		print(final_intv[i],end='	')

	print('')

if __name__ == '__main__':
	main()


"""
1 3
2 8
2 5
3 7
4 8
4 6
6 12
7 10
"""

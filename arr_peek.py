def main():

	A=[2,4,6,8,7,5,3]

	B=[10,12,8,4,-3,-15]

	print('\nThe array is:	',B)

	p=getPeek(B,0,len(B)-1)

	print("\nThe peek is:",p,'\n')

def getPeek(A,l,h):

	if (h-l)>0:

		m=l+(h-l)/2
		m=int(m)

		if A[m+1]>A[m]:
			return getPeek(A,m+1,h)
		else:
			return getPeek(A,l,m)

	else:
		return A[l]

if __name__ == '__main__':
	main()

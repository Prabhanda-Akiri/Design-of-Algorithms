def main():

	A=[1,3,9,8,5]

	B=[4,10,8,2,1]
	print('\nThe array is :	\n\nindex	element')

	for i in range(len(A)):
		print(i,'	',A[i])
	print('\n\n')

	inv=getInversions(A)

	print('\nThe total number of inversions are:	',inv)

def getInversions(A):

	count=0

	n=len(A)

	for i in range(n):
		for j in range(n):

			if (j>i and A[i]>A[j]):

				print('An inversion pair:	i=',i,'j=',j,'A[i]=',A[i],'A[j]=',A[j])

				count=count+1


	return count

if __name__ == '__main__':
	main()

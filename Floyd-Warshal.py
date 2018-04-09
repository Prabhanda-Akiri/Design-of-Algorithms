def main():

	n=int(input('\nnumber of vertices:	'))
	e=int(input('\nnumber of edges:	'))
	print('\nEnter the edges and their weights:	\n')

	E=[[0 for i in range(3)] for j in range(e)]
	for i in range(e):
		s=input()
		s=s.split()
		E[i][0]=int(s[0])
		E[i][1]=int(s[1])
		E[i][2]=int(s[2])

	fl=Floyd_Warshall(n,e,E)

	short_p=fl.apply()

	print(short_p)


class Floyd_Warshall:

	def __init__(self,n,e,E):

		self.n=n
		self.e=e 

		self.D=[None for i in range(n+1)]
		self.P=[None for i in range(n+1)]

		self.P[0]=[[None for i in range(self.n)] for i in range(self.n)]
		self.D[0]=[[99999 for i in range(self.n)] for j in range(self.n)]

		for i in range(n):
			for j in range(n):
				self.P[0][i][j]=i+1
				if i==j:
					self.D[0][i][j]=0

		for i in range(e):
			self.D[0][E[i][0]-1][E[i][1]-1]=E[i][2]

	def apply(self):

		for k in range(1,self.n+1):

			self.D[k]=[[99999 for i in range(self.n)] for j in range(self.n)] 
			self.P[k]=[[None for i in range(self.n)] for i in range(self.n)]

			for i in range(self.n):
				for j in range(self.n):

					if k<self.n and (self.D[k-1][i][k]!=99999 and self.D[k-1][k][j]!=99999):
						self.D[k][i][j]= min(self.D[k-1][i][j],(self.D[k-1][i][k] + self.D[k-1][k][j])) 
						self.P[k][i][j]=self.P[k-1][k][j]

					else:
						self.D[k][i][j]=self.D[k-1][i][j]
						self.P[k][i][j]=self.P[k-1][i][j]

		#print(self.P[self.n])

		for i in range(self.n):
			for j in range(self.n):
				print('predecessor of ',j+1,'in path from ',i+1, 'is:	',self.P[self.n][i][j])

		return self.D[self.n]


if __name__ == '__main__':
	main()

"""
6

10

4 1 -4
2 1 1
2 4 2
1 5 -1
4 5 3 
5 2 7
3 2 2 
6 2 5
6 3 10
3 6 -8

"""

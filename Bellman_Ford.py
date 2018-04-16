def main():

	n=int(input('\nEnter the number of vertices:	'))
	e=int(input('\nEnter the number of Edges:	'))
	print('Enter Edges:	\n')
	ed=[[] for i in range(e) ]

	for i in range(e):

		strng=input()
		x=strng.split(' ')
		ed[i].append(int(x[0]))
		ed[i].append(int(x[1]))
		ed[i].append(int(x[2]))

	adj=[[] for i in range(n)]
	adj_w=[[] for i in range(n)]

	for i in range(len(ed)):

		adj[ed[i][1]].append(ed[i][0])
		adj_w[ed[i][1]].append(ed[i][2])

	Bellman(n,e,adj,adj_w) 

def Bellman(n,e,adj,adj_w):

	T=[[99999 for i in range(n)] for j in range(n)]

	T[0]=[0 for i in range(n)]

	for k in range(1,n):
		for v in range(1,n):
			T[v][k]=T[v][k-1]

			for i in range(len(adj[v])):
				if T[v][k]>T[adj[v][i]][k-1]+adj_w[v][i] :
					T[v][k]=T[adj[v][i]][k-1]+adj_w[v][i]


	for i in range(n):
		print(T[i][n-1])

if __name__ == '__main__':
	main()
	

"""
0 1 1
1 2 2
"""

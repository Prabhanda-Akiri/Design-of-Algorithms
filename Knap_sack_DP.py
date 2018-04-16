def main():

	n=5
	v=[3,5,2,3,4]
	w=[2,4,2,4,1]

	C=10
	print(Knap_Sack(n,v,w,C))

def Knap_Sack(n,v,w,C):

	T=[[0 for i in range(n+1)] for j in range(C)]

	for i in range(0,C):
		T[C-1][n]=0 

	for i in range(n-1,-1,-1):
		for c in range(0,C):
			if w[i]>c :
				T[c][i]=T[c][i+1]
			else:
				if T[c-w[i]][i+1]!=None :
					T[c][i]=max(T[c][i+1],T[c-w[i]][i+1]+v[i])
				else:
					T[c][i]=T[c][i+1]

	return T[C-1][0]

if __name__ == '__main__':
	main()

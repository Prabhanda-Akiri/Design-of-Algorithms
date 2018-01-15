def main():

	n=5
	M=['Victor','Wyatt','Xavier','Yancey','Zeus']
	W=['Amy','Bertha','Clare','Diane','Erika']


	wPref=[[None for i in range(n)]for j in range(n)]
	mPref=[[None for i in range(n)]for j in range(n)]

	wPref=[[1,2,4,3,0],[3,1,0,2,4],[4,0,1,2,3],[0,4,3,2,1],[4,1,3,0,2]]
	mPref=[[1,0,3,4,2],[3,1,0,2,4],[1,4,2,3,0],[0,3,2,1,4],[1,3,0,4,2]]

	GaleShapley(M,W,n,wPref,mPref)

def GaleShapley(M,W,n,wPref,mPref):

	fMen=[0,1,2,3,4]
	wife=[None for i in range(n)]
	husb=[None for i in range(n)]
	pCount=[0 for i in range(n)]

	while(fMen and pCount[fMen[0]]!=5):


		m=fMen.pop(0)

		w=mPref[m][pCount[m]]
		pCount[m]=pCount[m]+1

		if(husb[w]==None):

			husb[w]=m 
			wife[m]=w 

		elif(wPref[w][husb[w]]>wPref[w][m]):

			fMen.append(husb[w])
			wife[husb[w]]=None
			husb[w]=m 
			wife[m]=w

		else:
			fMen.append(m)


	print('\n')
	for i in range(n):

		print(M[i],'---',W[wife[i]])
	print('\n')

if __name__ == '__main__':
	main()

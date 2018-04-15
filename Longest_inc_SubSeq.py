def main():

	S=[5,2,8,6,3,6,9,7]

	L=Longest_SubSeq(S)

	print('\nLength of Longest Increasing Subsequene: ',len(L),'\n\nLongest Subsequence is :	',L) 

def Longest_SubSeq(S):

	n=len(S)
	memo=[1 for i in range(n)]
	Max=0
	memo[0]=0 

	Subseq=[[S[i]] for i in range(n)]

	for i in range(1,n):
		maxm=1 
		for k in range(0,i):
			
			if S[k]<S[i]:
				if maxm < (memo[k] + 1) :
					maxm=memo[k] + 1 
					Subseq[i]=Subseq[k] + [S[i]]
		memo[i]=maxm

	#print(Subseq)
	Max=-1

	for i in range(0,n):
		if len(Subseq[i])>len(Subseq[Max]):
			Max=i 

	return Subseq[Max]

if __name__ == '__main__':
	main()

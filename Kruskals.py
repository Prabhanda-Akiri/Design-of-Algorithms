class Disj_Set:

	def __init__(self):
		self.v=[]

	def mkset(self,k):
		temp=Node()
		self.v.append(temp)
		temp.val=k
		temp.parent=temp
		temp.rank=0

	def fdset(self,a):

		initial=self.v[a]
		temp=initial
		final=None

		while(True):
			if temp.parent==temp:
				final=temp
				break
			temp=temp.parent

		initial.parent=final 
		return final

	def un(self,a,b):
		x=self.fdset(a)
		y=self.fdset(b)

		if x.rank>y.rank:
			y.parent=x

		elif x.rank<y.rank:
			x.parent=y

		else:
			x.parent=y
			y.rank+=1

	def printsets(self):
		
		for i in range(len(self.v)):

			print('\nVertex',i,':	',end=' ')
			temp=self.v[i]
			while(True):
				print(temp.val,end=' ')
				if temp.parent==temp:					
					break
				temp=temp.parent
		print('\n')


class Node:

	def __init__(self):

		self.parent=None
		self.val=None
		self.rank=0

def makeset():
	d=Disj_Set()
	d.mkset( )


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

	sorted_ed=sorted(ed,key=takeThird)

	Kruskals_Algo(n,sorted_ed)

def Kruskals_Algo(V,E):

	T=[]
	disj=Disj_Set()

	for i in range(V):
		disj.mkset(i)

	for i in range(len(E)):
		if disj.fdset(E[i][0])!=disj.fdset(E[i][1]):
			T.append(E[i])
			disj.un(E[i][0],E[i][1])
	print('Edges in MST\n',T)

def takeThird(elem):
    return elem[2]

if __name__ == '__main__':
	main()

"""
0 1 3
0 3 2
0 4 2
1 4 1
1 2 1
1 5 8
2 4 4
2 5 2
3 4 1
4 5 2
"""

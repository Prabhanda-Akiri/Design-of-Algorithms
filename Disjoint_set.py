class Disj_Set:

	def __init__(self):
		self.v=[]

	def makeset(self,k):
		temp=Node()
		self.v.append(temp)
		temp.val=k
		temp.parent=temp
		temp.rank=0

	def findset(self,a):

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

	def union(self,a,b):
		x=self.findset(a)
		y=self.findset(b)

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


def main():

	n=int(input('\nEnter the number of vertices:	'))
	e=int(input('\nEnter the number of Edges:	'))

	ed=[[] for i in range(e) ]

	for i in range(e):

		print('Edge ',i+1,end='')
		strng=input(':	')
		x=strng.split(' ')
		ed[i].append(int(x[0]))
		ed[i].append(int(x[1]))


	Connected_component(n,ed)

def Connected_component(V,E):

	disj=Disj_Set()

	for i in range(V):
		disj.makeset(i)

	for i in range(len(E)):

		if disj.findset(E[i][0])!=disj.findset(E[i][1]):
			disj.union(E[i][0],E[i][1])

	disj.printsets()

if __name__ == '__main__':
	main()

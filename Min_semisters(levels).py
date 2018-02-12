def main():

	n=7
	lists=[[0,1],[1,2],[2,3],[1,5],[4,5],[5,6]]

	adj_list=[[] for i in range(n)]

	for i in range(len(lists)):

		adj_list[lists[i][0]].append(lists[i][1])

	incoming_count=apply_DFS(adj_list,n)

	#print(incoming_count)

	num=solve_DAG(incoming_count,adj_list,n)
	print('Number of min. Semisters:	',num)


def apply_DFS(List,n):

	l=[0 for i in range(n)]

	count=0

	list_count=[]

	for i in range(n):
		list_count.append(i)

	while list_count:

		u=list_count.pop()

		for i in range(len(List[u])):

			l[List[u][i]]=l[List[u][i]]+1

	return l


def solve_DAG(count,adj_list,n):

	source_list=[]
	m=0
	state=[0 for i in range(n)]

	for i in range(n):
		if count[i]==0:
			source_list.append(i)
			state[i]=1

	while source_list:
		u=source_list.pop(0)
		for i in range(len(adj_list[u])):
			if state[adj_list[u][i]]==0:
				state[adj_list[u][i]]=state[u]+1
				source_list.append(adj_list[u][i])

	for i in range(n):
		if state[i]>m:
			m=state[i]

	return m
	
if __name__ == '__main__':
	main()

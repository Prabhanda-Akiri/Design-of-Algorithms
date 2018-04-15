import heapq

class Node:
    def __init__(self,s,f,y,x):

        self.freq=f 
        self.symbol=s
        self.left=y
        self.right=x

    def __lt__(self,other):
        return self.freq<other.freq

class Huffman:

    def __init__(self,S,F,n):

        self.S=S 
        self.F=F 
        self.n=n 
        self.leaves=[]
        self.heap=[]
        for i in range(n):
            leaf=Node(S[i],F[i],None,None)
            heapq.heappush(self.heap,leaf)
            self.leaves.append(leaf)

    

    def apply(self):

        for i in range(self.n-1):
            
            x=heapq.heappop(self.heap)
            y=heapq.heappop(self.heap)

            node=Node(None,(x.freq+y.freq),y,x)
            heapq.heappush(self.heap,node)

    def show_codes(self):

        self.root=heapq.heappop(self.heap) 
        self.recurse_print(self.root,[])

    def recurse_print(self,v,L):

        if v.left==None and v.right==None:
            print('Symbol : ',v.symbol,'    Code : ',end='  ')
            
            for i in range(len(L)):
                print(L[i],end='')
            print()

        else:
                L.append(0)
                self.recurse_print(v.left,L)
                if L :
                    L.pop(-1)
                L.append(1)
                self.recurse_print(v.right,L)
                if v.symbol==None:
                    L.pop(-1)


def main():

    n=6
    #n=int(input('\nEnter the number of Symbols:   '))
    print('\nSymbols and their corresponding frequencies....\n')
    S=['a','b','c','d','e','f']
    F=[20,12,10,8,4,3]

    """for i in range(n):
        s=input()
        s=s.split()
        S.append(s[0])
        F.append(s[1])"""

    h=Huffman(S,F,n)
    h.apply()
    h.show_codes()

if __name__ == '__main__':
    main()

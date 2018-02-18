class TreeNode:

    def __init__(self):

        self.parent=None
        self.left=None
        self.right=None
        self.value=0
        self.count=1

class Node:
    
    def __init__(self):
        self.next=None

class BST:

    def __init__(self,n):
        self.root=Node()
        self.n=n

    def insert(self,x):

        t=TreeNode()
        t.value=x
        temp=TreeNode()
        p=0
        if self.root.next==None:

            self.root.next=t
        else:

            temp=self.root.next
            te=self.root.next
            flag=0
            while temp!=None:
                if t.value>temp.value:
                    te=temp
                    temp=temp.right
                    p=1
                    
                elif t.value<temp.value:
                    te=temp
                    temp=temp.left
                    p=2
                elif t.value==temp.value:
                    temp.count+=1
                    flag=1
                    break;
                    
            if flag==1:
                if temp.count>self.n/2:
                    return temp.count  
            else:  
                t.parent=te
                if p==1:
                    te.right=t
                
                elif p==2:
                    te.left=t

        return

def main():

        A=[2,3,4,4,5,4,4,4]
        b=BST(len(A))
        flag=0
        major_ele=None

        for i in range(len(A)):
            ptr=b.insert(A[i])
            if ptr!=None:
                major_ele=A[i]
                flag=1

        if flag!=1:
            print('No majority element..!!')
        else:
            print('Majority element is: ',major_ele,'\nIt occurs ',ptr,' times')

if __name__ == '__main__':
    main()


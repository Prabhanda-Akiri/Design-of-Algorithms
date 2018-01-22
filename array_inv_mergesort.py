def main():

    A=[1,3,9,8,5]

    low=0
    high=len(A)-1
    count=0
    print('Array before sorting:',A)
    count=sort_and_count_inv(A,low,high)
    print('\n\nArray after sorting (MERGE sort):\n','                 ',A,'\n\nNumber of inversions :   ',count,'\n\n')



def sort_and_count_inv(A,low,high):

    if low<high:

        mid=int(low+(high-low)/2)
        a,b,c=0,0,0

        a=sort_and_count_inv(A,low,mid)
        b=sort_and_count_inv(A,mid+1,high)

        c=sort_and_count_split(A,low,mid,high)

        return a+b+c
    return 0

def sort_and_count_split(A,low,mid,high):

    n1=mid-low+1
    n2=high-mid
    L=[]
    R=[]
    c=0
    for i in range(0,n1):

        L.append(A[low+i])

    for i in range(0,n2):

        R.append(A[mid+1+i])

    l=0
    r=0
    i=low

    while(l<n1 and r<n2):

        if L[l]>R[r]:

            A[i]=R[r]
            r=r+1
            c=c+n1-l
        else:

            A[i]=L[l]
            l=l+1

        i=i+1

    
    while l<n1:

        A[i]=L[l]
        l=l+1
        i=i+1               

    while r<n2:

        A[i]=R[r]
        r=r+1
        i=i+1

    return c


if __name__ == '__main__':
    main()

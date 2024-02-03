file=open('input4.txt')
size=int(file.readline())
file=file.read()
arr=[0]*size
arr=[int(x) for x in file.split()]
def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(n1):
        L[i]=A[p+i-1]
    for j in range(n2):
        R[j]=A[q+j]
    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    i = j= 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + (r-1) )// 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
mergeSort(arr,0,len(arr)-1)
new_file=open('output4.txt','w')
for i in arr:
    new_file.write(str(i)+' ')


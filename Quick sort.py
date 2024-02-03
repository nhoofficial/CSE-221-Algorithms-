import random
c=0
def partition(a,p,r):
    pivot=a[p]
    i=p
    for j in range(i+1,r+1):
        if pivot>=a[j]:
          i += 1
          temp=a[i]
          a[i]=a[j]
          a[j]=temp

    a[p],a[i] = a[i], a[p]

    return i
def quicksort(a,p,r):
  if p<r:
    q=partition(a,p,r)
    quicksort(a,p,q-1)
    quicksort(a,q+1,r)

a=[6,10,13,5,3,8,2,11]
quicksort(a,0,len(a)-1)
for i in a:
    print(i)

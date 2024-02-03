def merge(a,b):
    c=[0]*(len(a)+len(b))
    i=0
    j=0
    k=0
    while k<=len(c):   #O(n)
        if i<len(a) and j<len(b):
            if a[i]<=b[j]:
                c[k]=a[i]
                i+=1
                k+=1
            else:
                c[k]=b[j]
                j+=1
                k+=1
        else:
            break
    if i<len(a)-1:
        c[k]=a[i]
        k+=1
        i+=1
    else:
        c[k]=b[j]
        k+=1
        j+=1
    return c

def merge_sort(A):
    n=len(A)
    if n==1:
        return A
    else:
        a1=merge_sort(A[:n//2]) #time_complexity O(log_2 n)
        a2=merge_sort(A[n//2:])
        merge(a1,a2) #O(n log_2 n)

#a=[1,7,9,12,20]
#b=[4,8,11,22]
a=[23,12,34,6,43,1]
print(merge_sort(a))



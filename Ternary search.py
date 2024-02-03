def ternary_search(a,l,r,val):
    mid1=l+(r-3)//3
    mid2=r-(r-l)//3
    if l>r:
        return -1
    if a[mid1] == val or a[mid2] == val:
        return True
    else:
        if a[mid1]>val:
            return ternary_search(a,l,mid1-1,val)
        elif a[mid1]<val and a[mid2]<val:
            return ternary_search(a,mid2+1,r,val)
        else:
            return ternary_search(a,mid1+1,mid2-1,val)

a=[78,120,129,369,444,525]
print(ternary_search(a,0,len(a)-1,000))
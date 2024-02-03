inputFile=open('input2.txt')
n,size=inputFile.readline().split(' ')
inputFile=inputFile.read()
arr=[0]*int(n)
arr=[int(x) for x in inputFile.split()]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=arr[i]
        min_idx=i
        for j in range(i+1,n):
            if min>arr[j]:
                min=arr[j]
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

    return arr
c=selection_sort(arr)
newfile=open('output2.txt','w')
for i in range(int(size)):
    newfile.write(str(c[i])+" ")
inputFile=open('input3.txt')
size=int(inputFile.readline())
inputFile=inputFile.read()
idx=[int(x) for x in inputFile.split()]

arr={}
A=[]
index=size
for i in range(size):
    arr[idx[i]]=idx[index]
    index+=1

for i in arr.values():
    A.append(i)

def insertion_sort(A):
    n = len(A)
    for i in range(0, n-1):
        temp = A[i + 1]
        j=i
        while j>=0:
            if A[j] > temp:
                A[j + 1] = A[j]
            else:
                break
            j-=1

        A[j+1] = temp
    return A
c=insertion_sort(A)
c.reverse()
newfile=open('output3.txt','w')
new_array=[]
for i in c:
    if i in arr.values():
        for x,y in arr.items():
            if i==y and x not in new_array:
                new_array.append(x)
for i in new_array:
    newfile.write(str(i)+' ')



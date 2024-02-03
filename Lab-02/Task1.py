inputFile=open('input1.txt')
size=int(inputFile.readline(1))
inputFile=inputFile.read()
arr=[0]*size
arr=[int(x) for x in inputFile.split()]
def bubble_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        if i>0:
            if arr[i] < arr[i - 1]:
                #   Explanation: As in the bubble sort, we compare each element with another. Suppose, i=0 and a[i-1]=45 and a[i]=28
                #                so a[i]<a[i-1] then the second loop will execute.
                #                For example, for the best case scenraio our input array a=[1,2,3,4,5,6] then the second will execute O times.
                #                Then the time complexity of the following code will be θ(n) instead of θ(n^2).
                for j in range(0, i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr
newfile=open('output1.txt','w')
c=bubble_sort(arr)
for i in c:
    newfile.write(str(i)+" ")

output=open('output1.txt','w')
file = open('task1_input.txt')
test=int(file.readline())
assi={}
for i in range(test):
    n,m=file.readline().split()
    assi[int(n)]=int(m)
max_key = max(assi)
arr=[0]*(max_key+1)
for x,y in assi.items():
    arr[x]=[y]
min_key = min(assi)
queue={min_key:arr[min_key][0]}

c=1
f=arr[min_key][0]
for i in range(len(arr)):
    if i in assi:
        if i>=f:
            c+=1
            f=arr[i][0]
            queue[i]=assi[i]
output.write(str(c)+'\n')
for x,y in queue.items():
    output.write(str(x)+' '+str(y)+'\n')




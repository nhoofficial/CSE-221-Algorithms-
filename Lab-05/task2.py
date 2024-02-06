
output=open('output2.txt','w')
file = open('task2_input.txt')
test,a=file.readline().split(' ')
test,a=int(test),int(a)

assi={}
for i in range(test):
    n,m=file.readline().split()
    assi[int(n)]=int(m)

max_key = max(assi, key=assi. get)
arr=[0]*(max_key+1)
for x,y in assi.items():
    arr[x]=[y]

min_key = min(assi, key=assi. get)

queue={min_key:arr[min_key][0]}
c=1
c1=1
f=arr[min_key][0]
f1=arr[min_key+1][0]
for i in range(min_key,len(arr)):
    if i in assi.keys():
        if i>=f:
            c+=1
            f=arr[i][0]
            queue[i]=assi[i]
    if i in assi.keys():
        if i>=f1:
            c1+=1
            f1=arr[i][0]
            queue[i]=assi[i]

output.write(str(c+c1)+'\n')


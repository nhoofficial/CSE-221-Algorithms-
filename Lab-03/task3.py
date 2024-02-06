from task1 import graph
from task1 import noOfPlacesOrNodes#lab 05

#task1
a=open('input1.txt','w')
s=[]
f=[]
n=int(a.readline())
output=open('output1.txt','w')
for i in range(n):
    x,y=input().split()
    x,y=int(x),int(y)
    s.append(x)
    f.append(y)

def printMaxActivities(s, f):
    n = len(f)
    i = 0
    output.write(str(i))
    for j in range(n):
        if s[j] >= f[i]:
            output.write(str(j))
            i = j
printMaxActivities(s, f)


#task02
a=open('input1.txt','w')
s=[]
f=[]
n=int(a.readline())
output=open('output1.txt','w')
for i in range(n):
    x,y=input().split()
    x,y=int(x),int(y)
    s.append(x)
    f.append(y)

def printMaxActivities(s, f):
    n = len(f)
    i = 0
    output.write(str(i))
    for j in range(n):
        if s[j] >= f[i]:
            output.write(str(j))
            i = j
c=1
d=1
n1=f[0]
n2=f[0+1]
for i in range(min_key,len(arr)):
    if i in n1:
        if i>=n1:
            c+=1
            n1=f[i]
    if i in n1:
        if i>=n2:
            n2=f[0]
            d += 1
output.write(str(c+d)+'\n')
printMaxActivities(s, f)
visited =[0]*noOfPlacesOrNodes
printed = []
outputFile2=open('output2.txt','w')
def DFS_VISIT(graph,node):
    visited[int(node)-1]=1
    printed.append(node)
    for node in graph[node]:
        if node not in visited:
            DFS_VISIT(graph,node)
def DFS(graph,endPoint):
    for node in graph:
        if node not in visited:
            DFS_VISIT(graph,node)
    for i in range(endPoint):
        if printed[i]==endPoint:
            outputFile2.write(str(printed[i]) + ' ')
            break
        else:
            outputFile2.write(str(printed[i])+' ')

DFS(graph,12)
file=open('input1.txt')
noOfPlacesOrNodes=int(file.readline())
graph={}
for i in range(1,noOfPlacesOrNodes+1):
    list=[]
    new=[]
    list=[int(x) for x in file.readline().split(' ')]
    c=list[0]
    for k in range(1,len(list)):
        if list[k]!='\n':
            new.append(list[k])
    graph[c]=new
print(graph)
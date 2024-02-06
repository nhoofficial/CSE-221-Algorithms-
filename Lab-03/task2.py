from task1 import graph
from task1 import noOfPlacesOrNodes
outputfile1=open('output1.txt','w')
##############################################################
visited =[0]*noOfPlacesOrNodes
queue =[]
def BFS(visited, graph, node, endPoint):
    visited[int(node)-1]=1
    queue.append(node)
    while queue!=None:
        m=queue.pop(0)
        outputfile1.write(str(m)+' ')
        if m==endPoint:
            break
        for neighbour in graph[m]:
            if visited[int(neighbour)-1]==0:
                visited[int(neighbour)-1]=1
                queue.append(neighbour)
BFS(visited, graph, 1, 12)
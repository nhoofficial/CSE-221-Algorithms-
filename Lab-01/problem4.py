file=open('input4.txt')
n=int(file.readline(1))
file.readline()
A = []
B = []

for i in range(n):
    arr=[int(x) for x in file.readline().split()]
    A.append(arr)
file.readline()
for i in range(n):
    arr=[int(x) for x in file.readline().split()]
    B.append(arr)

def Multiply_matrix(A, B):
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C
result_matrix=Multiply_matrix(A,B)
newfile=open('output4.txt','w')
for i in result_matrix:
    for j in i:
        newfile.write(str(j) + " ")
    newfile.write('\n')
input1=open('task1_input.txt')
zone=int(input1.readline())
X=input1.readline()
Y=input1.readline()
output1=open('output1.txt','w')

def LCS(X,Y):
    m=len(X)+1
    n=len(Y)+1
    c =[[0]*(n) for i in range(m)]
    t =[[0]*(n) for i in range(m)]
    for i in range(1,m):
        c[i][0]=0
        t[i][0]=None
    for j in range(1,n):
        c[0][j]=0
        t[0][j]=None

    for i in range(1, m):
        for j in range(1, n):
            if (X[i - 1] == Y[j - 1]):
                c[i][j] = c[i - 1][j - 1] + 1
                t[i][j] = 'diagonal'
            elif (c[i - 1][j] >= c[i][j - 1]):
                c[i][j] = c[i - 1][j]
                t[i][j] = 'up'
            else:
                c[i][j] = c[i][j - 1]
                t[i][j] = 'left'

    idx = c[m-1][n-1]
    lcs = ''
    i = m-1
    j = n-1
    while i > 0 and j > 0:
        if t[i][j]=='diagonal':#diagonal
            lcs += X[i - 1]
            i -= 1
            j -= 1
            idx -= 1

        elif c[i - 1][j] > c[i][j - 1]:#up
            i -= 1
        else:
            j -= 1#left
    new=lcs[::-1]
    return c[m-1][n-1],new
a,b=LCS(X,Y)
correctness=(a*100)/zone
for i in b:
    if i=='Y':
        output1.write('Yasnaya ')
    elif i=='P':
        output1.write('Pochinki ')
    elif i=='S':
        output1.write('School ')
    elif i=='R':
        output1.write('Rozhok ')
    elif i=='F':
        output1.write('Farm ')
    elif i=='M':
        output1.write('Mylta ')
    elif i == 'H':
        output1.write('Shelter ')
    else:
        if i=='I':
            output1.write('Prison ')
try:
    correctness=int(correctness)
    output1.write('\n'+'Correctness of prediction: '+"".join(str(correctness))+'%' )
except:
    output1.write('\n' + 'Correctness of prediction: {}%'.format(correctness))
output1.close()
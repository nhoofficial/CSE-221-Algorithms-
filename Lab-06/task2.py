input2=open('task2_input.txt')
X=input2.readline()
Y=input2.readline()
Z=input2.readline()
output2=open('output2.txt','w')

def LCS(X,Y,Z):
    m=len(X)+1
    n=len(Y)+1
    o=len(Z)+1
    c =[[[0 for i in range(o)] for j in range(n)] for k in range(m)]
    t=[[[0 for i in range(o)] for j in range(n)] for k in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1,o):
                if i==0 or j ==0 or k==0:
                    c[i][j][k]=0
                    t[i][j][k]=None
                else:
                    if X[i-1]==Y[j-1] and X[i-1] == Z[k-1]:
                        c[i][j][k]=1+c[i-1][j-1][k-1]
                        t[i][j][k]='diagonal'
                    else:
                        if c[i-1][j][k]>=c[i][j-1][k]:
                            max=c[i-1][j][k]
                            if max>=c[i][j][k-1]:
                                c[i][j][k]=max
                                t[i][j][k]='up-up-left'
                            else:
                                max=c[i][j][k-1]
                                c[i][j][k]=max
                                t[i][j][k]='left-up-up'
                        else:
                            max=c[i][j-1][k]
                            if max>=c[i][j][k-1]:
                                c[i][j][k]=max
                                t[i][j][k]='up-left-up'
                            else:
                                max=c[i][j][k-1]
                                c[i][j][k]=max
                                t[i][j][k]='left-up-up'
    return c[m-1][n-1][o-1]
a=LCS(X,Y,Z)
output2.write(str(a))
output2.close()
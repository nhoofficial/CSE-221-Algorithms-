q=[]
output=open('output3.txt','w')
file = open('task3_input.txt')
test=int(file.readline())
a=[int(x) for x in file.readline().split()]
a.sort()
string=file.readline()
h1=''
index=0
for c in string:
    if c=='J':
        q.append(a[index])
        h1+=str(a[index])
        index += 1
    else:
        if c=='j':
            n=q[-1]
            h1+=str(n)
            q.pop()
jack=0
jill=0
output.write(h1+'\n')
i=0
while i<len(h1):
    if string[i]=='J':
        jack+=int(h1[i])
    else:
        jill+=int(h1[i])
    i+=1

output.write('Jack will work for {} hours'.format(jack)+'\n'+'Jill will work for {} hours'.format(jill))




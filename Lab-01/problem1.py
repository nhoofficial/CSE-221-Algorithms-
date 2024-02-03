file = open('input.txt')
file= file.read()
newfile = open('output.txt','w')
lst = file.split('\n')
even_c=0
odd_c=0
noparity_c=0
notpalindrome_c=0
palindrome_c=0
def isPalindrome(lst):
    global even_c
    global odd_c
    global noparity_c
    global palindrome_c
    global notpalindrome_c
    total_parity=0
    total_palindrome=0
    if lst==None:
        return f'not palindrome'
    else:
        list_1 = []
        list_2 = []
        for data in lst:
            if data != "":
                word, num = data.split()
                list_1.append(word)
                list_2.append(num)

        for i in range(len(list_1)):
            try:
                list_1[i]=int(list_1[i])
            except:
                list_1[i]=float(list_1[i])
            if type(list_1[i])==int:
                if list_1[i]%2!=0:
                    newfile.write(str(list_1[i])+' has odd parity')
                    odd_c+=1
                    total_parity+=1
                else:
                    newfile.write(str(list_1[i]) + ' has even parity')
                    even_c+=1
                    total_parity+=1
            else:
                newfile.write(str(list_1[i]) + ' can not have parity')
                noparity_c+=1
                total_parity+=1
            new = ''
            string = list_2[i]
            new = string[len(string) - 1::-1]

            if new==list_2[i]:
                newfile.write(' and '+list_2[i]+' is a palindrome.')
                palindrome_c+=1
                total_palindrome+=1
            else:
                newfile.write(' and ' + list_2[i] + ' is not a palindrome.')
                notpalindrome_c+=1
                total_palindrome+=1
            newfile.write('\n')
        newfile2=open('record.txt','w')
        newfile2.write('Percentage of odd parity: '+str(int((odd_c*100)/total_parity))+'%\n')
        newfile2.write('Percentage of even parity: ' + str(int((even_c * 100) / total_parity)) + '%\n')
        newfile2.write('Percentage of no parity: ' + str(int((noparity_c * 100) / total_parity)) + '%\n')
        newfile2.write('Percentage of palindrome: ' + str(int((palindrome_c * 100) / total_palindrome)) + '%\n')
        newfile2.write('Percentage of non-palindrome: ' + str(int((notpalindrome_c * 100) / total_palindrome)) + '%\n')

isPalindrome(lst)

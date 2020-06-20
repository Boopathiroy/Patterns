
#character pattern not repeating the letters by boopathi

n = int(input("Enter a number: "))

#initialising num with ASCII value of A which is 65
num = 65
for i in range(0,n):
    for j in range(0,i+1):
        ch = chr(num)
        print(ch,end=' ')
        num +=1
    print('\r')
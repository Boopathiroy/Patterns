
#Pyramid patter by boopathi
#Method 1

n = int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print('* ',end='')
    print('\r')

#Method 2

n = int(input("Enter a number :"))
li = []
for i in range(0,n):
    li.append('*'*i)
print('\n'.join(li))
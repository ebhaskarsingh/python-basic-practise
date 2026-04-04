# wap to print numbers from  1 to n\\

n = int(input("enter the number: "))

for i in range(1,n+1):
    print(i)

# wap to print the sum of first n numbers\\

n = int(input("enter the number:"))
sum =0
for i in range(1,n+1):
    sum = sum+i
print("the sum is:",sum)

# wap to print the multiplication table of a number\\

n = int(input("enter the number :"))

for i in range(1,11):
    print(n,"*",i,"=",i*n)
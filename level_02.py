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

# wap to count the digits in a number\\

n = int (input("enter the number:"))
count = 0
for i in str(n):
    count = count+1

print("the total number in a given digit is:",count)


# wap to reverse the number\\

n = int(input("enter the number:"))
reverse = 0
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n = n//10

print(reverse)

# wap to check whether the number is palindrome or not\\

n = int(input("etner the number:"))
reverse = 0
num = n
while n>0:
    digits = n%10
    reverse = reverse*10+digits
    n = n//10

if num == reverse:
    print("it is palindrome")
else:
    print("it is not palindrome")

# wap to findt the factorial of a number\\

n = int(input("enter the number:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(fact)


# wap to find the nth fibonacci number\\

num = int(input("enter thr number:"))
first = 0
second = 1
sum = 0
if num == 0:
    print(first)
elif num == 1:
    print(second)
else:
    for i in range(2,num):
        
        sum = first+second
        first = second
        second = sum
    print(sum)


# wap to count odd and even numbers from given list\\

l = [1,2,3,4,5,6,7,8,9]
even =0
odd = 0
for i in l:
    if i%2==0:
        even = even+1
    else:
        odd = odd+1

print("even number:",even)
print("odd numbers:",odd)

# wap to find the GCD of two numbers\\
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
gcd = 1
for i in range(1,min(num1,num2)+1): # here min(num1,num2) will pick the smaller number between num1 and num2 \\
    if num1%i==0 and num2%i == 0:
        gcd = i
print(gcd)
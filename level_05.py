# wap to reverse the string\\

str = input("enter the string:")
print(str[::-1]) # slicing method to reverse the strin\

rev = ""
for i in str:
    rev = i+rev

print(rev) #  using loop to reverse the string\\


# wap to check whether the string is palindrome or not\\
string = input("enter the string:")
if string == string[::-1]:
    print("true")
else:
    print("false")


# wap to find the largest number in a list\\
l=[1,2,3,4,5]
first = l[0]
for i in l:
    if i>first:
        first = i
print(first)

# wap to find the index where the target met\\]

l = [1,2,3,4,5]
target = 3
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(i,j)
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
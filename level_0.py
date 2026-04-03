# take input from user and print it\\

user = input("enter your name:")
print("hello:",user)

# swap two variables with temp\\

a = 5
b = 10
temp = 0
print(a,b)
temp =a
a = b
b = temp
print(a,b)

# swap two variable without temp\\\

a = 5
b = 10
print(a,b)
a,b = b,a

print(a,b)

# wap to find the area of circle\\
r = int(input("enter the radius of circle:"))
pi = 3.14

print(f"area of circle is:{pi*r*r}")

# wap to convert the seconds into minutes\\

seconds = int(input("enter seconds:"))
minutes = seconds//60
print("minutes:",minutes)
# also convert it into hours\\
hours = float(seconds//3600)
print("hours:",hours)
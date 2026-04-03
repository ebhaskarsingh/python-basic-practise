# wap to check if number is even or odd\\

num = int(input("enter the number:"))
if num%2 == 0:
    print("even")
else:
    print("odd")



# wap to check if number is positive , negative or zero\\

num1 = int(input("enter the number1:"))
if num1>0:
    print("positive")
elif num1<0:
    print("negative")
else:
    print("zero")

# wap to find the largest number among three numbers\\

num1 = int(input("enter the number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

# wap to find the leap year\\
leap  = int(input("enter the year:"))
if leap %4 == 0 and leap%100!=0 :
    print("it is leap year")
else:
    print("it is not leap year")
           

# wap to check if the character is vowel or consonant\\

char = input("enter the character:")
vowels = "aeiouAEIOU"
if char in vowels:
    print("it is vowel")
else:
    print("it is consonant")


# wap to find if number is divisible by 5 and 11 \\

num = int(input("enter the number:"))
if num%5==0 and num%11==0:
    print("it is divisible by 5 and 11")
else:
    print("it is not divisible by 5 and 11")
           
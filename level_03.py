'''# wap to reverse a string\\
string = input("enter the string:")
reverse = string[::-1]
print(reverse)

# wap to check if the string is palindrome or not\\
string = input("enter the string:")
reverse = string[::-1]
if reverse == string:
    print("it is palindrome")
else:
    print("it is not palindrome")


# wap to count the number of vowels and consonants in a string\

string = input("enter the string:")
vowels = 0
consonants = 0
for i in string:
    if i in "aeiouAEIOU":
        vowels+=1
    else:
        consonants+=1

print("vowels:",vowels)
print("consonants:",consonants)

# wap to replace spaces from string\\

string = input("enter the string:")
new_string = string.replace(" ","")
print(new_string)

# wap to convert the lowercase into uppercase without using inbuilt function\\

character = input("enter the character:")
uppercase = chr(ord(character)-32)
print(uppercase)

# wap to find the frequency of each character in a string\\

string = input("enter the string:")
string1 = set(string)
for i in string1:

    count = string.count(i)
    print(i,":",count)'''

# wap to find the largest word in a string\\

string = input("enter the sentence:")
string1 = string.split()
largest = ""
for i in string1:
    if len(i)> len(largest):
        largest=i
print("the largest word is :",largest)

# wap to replaces spaces with hyphens in a string\\
string = input("enter the string:")
new_string = string.replace(" ","-")
print(new_string)

# wap to find whether the two strings are anagrams or not\

string1 = input("enter the first string:")
string2 = input("enter the second string:")
if sorted(string1) == sorted(string2):
    print("it is anagram")
else:
    print("it is not anagram")

# wap to count words in a string\\

string = input("enter the sentence:")
string1 = string.split()
count = 0
for i in string1:
    count = count+1

print("the total number of words in a given string is:",count)
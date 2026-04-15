# wap to find the maximum and minimum number in a list\\

l = [1,2,3,4,5,6,9,8,7]
print("maximum number is:",max(l))
print("minimum number is:",min(l))


# wap to print the sum of list \\

l = [1,2,3,4]
sum1 = 0
for i in l:
    sum1+=i
print("the sum is:",sum1)
total = sum(l) # we can find the sum of list by using inbuilt function sum() also\\
print(total)

# wap to remove the duplicate from list\\
l = [1,2,3,1,2]
l = list(set(l))# we can remove the duplicate from list by using set() function also\\
print(l)

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

# wap to reverse the list\\

l = [1,2,3,4]
reverse = l[::-1]
print(reverse)

# wap to find the second largest number in a list\\

l = [0,0,2,3,4,5]
first = 0
second = 0
for i in l:
    if i>first:
        second = first
        first = i
    elif i>second and i!=first:
        second = i
print("the second largest number is:",second)

# wap to merge two lists \\

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

# wap to sort list without using list function\\

l = [5,2,3,1,4]
n = len(l)
for i in range(n):
    for j in range(0, n-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)

# wap to find the common elements in two lists\\
l1 = [1,2,3]
l2 = [3,4,5]
l1.sort()
l2.sort()
common = []
for i in l1:
    if i in l2:
        common.append(i)
print("the common elements are:",common)

# i want to try abother technique\\
l1 = [1,2,3]
l2 = [3,4,5]
common = []
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i] == l2[j]:
            common.append(l1[i])
print("the common elements are:",common)

# count the frequency of each element in a list\\
l = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
nums = [2, 3, 1, 5, 6, 4, 0]
# print(sorted(nums)) # sorted() will returns a list
# print(nums.sort()) # sort() will returns a None, used with only list methods.
l = [1,2,3,8,9,5,7,6,4]
l1 = [1,3,5,7,8,10]
l2 = [2,3,4,6,8,9,10]
print(list(set(l1+l2)))

# sort a list without any inbuilt method
n = [3,2,1,5,4,6,7,8]
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] >= n[j]:
            n[i],n[j] = n[j],n[i]

# common elements between two lists.
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

lst = []
for i in list_a:
    if i in list_b:
        lst.append(i)
print(lst)

# Middle Element in a List
numList = [1, 2, 3, 4, 5,6,7]
midElement = int((len(numList)/2)) 
print(numList[midElement])

# Counting the occurrences of elements in the list
days = ['S','M','M','M','F','S']
y = set(days)
print([[i,days.count(i)] for i in y])

# Find Missing Number in an Array
n = [1, 2, 3, 5, 6, 7, 8, 9,10,11,13,14,16]
num = set(n)
op = []

for i in range(1, n[-1]):
    if i not in num:
        op.append(i)
print(op)

# Find Duplicate Number in an Array
lis = [1, 2, 2, 3, 4, 4, 4, 5, 5]
uniq_list = []
dup_list = []

for i in lis:
    if i not in uniq_list:
        uniq_list.append(i)
    elif i not in dup_list:
        dup_list.append(i)
print(dup_list)

# Find the number occurring odd number of times
lis = [1, 1, 2, 2, 3, 3, 3]
res = 0
for i in lis:
    res = res ^ i
print(res)

# count a total number in "n = 123654" have
n = 123654
count = 0
while(n>0):
    count += 1
    n = n//10
    # print("n = ",n,"count = ",count)
print("total number of digits", count)

# count even and odd from given list
even = 0
odd = 0
for x in l:
    if x%2 == 0:
        even += 1
    else:
        odd += 1
print("Total even number ", even," Total odd number ", odd)

my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[1][3])

# """1 2 3 4 tom 6 cat 8 9 tom 11 12 13 cat tom 16 17 18 19 tom """
for i in range(1,20+1):
    if i % 5 == 0 or i % 10 == 0:
        i = 'tom'
    elif (i % 7 == 0) or (i % 14 == 0):
        i = "cat"
    # print(i)
        
"""
Count All The 2 From given array
"""
arr=[1,2,2,3,4,5,6,2,7,8,9,2,8]
count = 0
match = 2

for i in range(len(arr)):
    if arr[i] == match:
        count = count+1
print("count",count)

# For example, the factorial of 6 is 1*2*3*4*5*6 = 720

num = 6
fact = 1

if num < 0:
    print("Factoril is Not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact *= i
    print("Factoril is = ", fact)
    
# Leap year
# year = 1994
# year = 2017
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

"""
* * * * *
* * * *
* * *
* *
*
"""
n = 5
for i in range(0,n+1):
    for j in range(1, n-i+1):
        print("*",end=" ")
    print()

"""
        *
      * *
    * * *
  * * * *
"""
n = 5
k = (n*2) - 2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k = k -2
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")

"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")

for i in range(0,n+1):
    for j in range(0,i-1+1):
        print("*",end=" ")
    print()

"""
     *
    ***
   *****
  *******
   *****
    ***
     *
"""
h = 7

if h%2 == 0:
    print("Enter the height odd number")
else:
    middle_row = (h+2)//2
    for i in range(middle_row):
        print(" " * (middle_row-i), "*" * (i*2+1))

    for i in range(middle_row-2,-1,-1):
        print(" " * (middle_row-i), "*" * (i*2+1))

"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""
k=1
i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ",end=" ")
        b=b+1
    j=1
    while(j<=k):
        print(j,end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1

# split
i = "manoj_parmar_india.json"
print(i.split('_'))
print(i.split('_')[::-1])
print(i.split('_')[::-1][0])
print(i.split('_')[::-1][0].split('.'))
print(i.split('_')[::-1][0].split('.')[0])
print(i.split('_')[::-1][0].split('.')[0].capitalize())

# flyod
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
count = 1

for i in range(1,n+1):
    for j in range(0,i):
        print(count,end=" ")
        count += 1
    print()

#Remove repeat character for string
s = "innage" 
print((list(set(s))))

# Remove repeated number from list and count a number how many times apper.
n=[5,2,1,4,3,2,8,4,2,1,2,0]
count = 0
c = []
l=[]
for i  in range(len(n)):
    if n[i] not in l:
        l.append(n[i])
        count = n.count(n[i])
        c.append(count)

l = [11,22,30,8,35] #if > 20 -1, < 20 -2
print([x-1 if x > 20 else x-2 for x in l])

# reverse a list, without any built in function or slicing.
lst = [1, 2, 3, 4, 5]
r_list = []
for value in lst:
    print(value)
    r_list = [value] + r_list
print("List after reverse : ", r_list)

# count and remove duplicates from list and then convert list to dictinory.
l = [11,22,11,30,8,35,8,8,22]
d = {}
a = []
b= []
c = 0
for i in l:
  if i not in a:
    a.append(i)
    c = l.count(i)
    b.append(c)
print(a,b)
for key in a:
  for value in b:
    d[key] = value
    b.remove(value)
    break
print(str(d))

t=['a','b','b','a','c','b']

dd = {}
for x in t:
    if x in dd:
      dd[x] += 1
    else:
      dd[x] = 1
print(dd)

# Reverse a number & string
n = 123456
rev = 0
while (n>0):
  a = n % 10
  rev = rev * 10 + a
  n = n//10
print(rev)

s = "manoj"
r = ''
for i in s:
  r = i + r
print(r,s[::-1])
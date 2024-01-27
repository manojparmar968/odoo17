# 1. Access Items
# Note.--> -1 refers to the last item, -2 refers to the second last item.
thislist = ["apple", "banana", "cherry"]
print(thislist[1],thislist[2:5]) 

# 2. Change Item Value
thislist = ["apple", "banana", "cherry","blackcurrant", "watermelon"]
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
    # A. Insert Items using insert()
thislist.insert(2, "watermelon")
print(thislist)

# 3. Add List Items
    # A. append() method
thislist.append("orange") # 
    # B. insert() method
thislist.insert(1, "orange") 
    # c. extend() method
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# 4. Remove List Items
    # A. remove(), have 2 items with same name so it will remove first one.
thislist.remove("banana")
    # B. pop() method, do not specify the index, the pop() method removes the last item.
thislist.pop(1)
    # c. del keyword,  also delete the list completely if not specify index.
del thislist[0]
    # D. clear() method,empties the list. The list still remains, but it has no content
thislist.clear()
print(thislist)

# 5. List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

# 6. Sort Lists
    # A. sort() method, 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # sort the list alphanumerically, ascending, by default
thislist.sort(reverse = True) # sort descending if user reverse = True
    # B. reverse()
thislist.reverse()
print(thislist,thislist[::-1])

# 7. Copy Lists
    # A. copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
    # B. list() method
mylist = list(thislist)

# 8. count()
x = fruits.count("cherry")

# 9. index()
x = fruits.index("cherry")
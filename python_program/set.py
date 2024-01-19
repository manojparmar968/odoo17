# 1. Add Set Items
    # A. add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
    # B. update() method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
mylist = ["kiwi", "orange"]
thisset.update(mylist) # (tuples, lists, dictionaries etc.).
# 2. Remove Set Items
    # A. Remove Item
        # 1. remove(), or discard() method 
thisset.remove("banana") # does not exist, remove() will raise an error.
thisset.discard("banana") # does not exist, discard() will NOT raise an error.
    # B. pop() method, will remove a random item
x = thisset.pop()
    # C. clear() method, empties the set
thisset.clear()
    # D. del keyword, delete the set completely
del thisset
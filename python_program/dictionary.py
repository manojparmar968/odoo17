# 1. Access Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
    # A. get()
x = thisdict.get("model")
    # B. keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
thisdict["color"] = "white"
    # C. values() method will return a list of all the values in the dictionary.
x = thisdict.values()
    # D. items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()

# 2. Change Dictionary Items / Adding Items
    # A. Change Values
thisdict["year"] = 2018
    # B. update()
thisdict.update({"year": 2020})

# 3. Remove Dictionary Items
    # A. pop() method removes the item with the specified key name.
thisdict.pop("model")
    # B. popitem() method removes the last inserted item
thisdict.popitem()
    # C. del keyword
del thisdict["model"]
del thisdict # cause an error because "thisdict" no longer exists.
    # D. clear() method empties the dictionary
thisdict.clear()

# 4. Copy Dictionaries
    # A. Copy a Dictionary
mydict = dict(thisdict)
    # B. copy() method
mydict = thisdict.copy()

# 5. fromkeys() method
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)

# 6. setdefault() method
x = thisdict.setdefault("color", "white")
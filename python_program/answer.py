arr=[0,1,2,2,3,4,5,6,2,7,8,9,2,8,0]
print(list(set(arr)))
print(arr.count(2))
print()

c = 0
ct = []
new_list = []
for i in arr:
  if i == 2:
    c += 1
  if i not in new_list:
    new_list.append(i)
    c = arr.count(i)
    ct.append(c)
print(c,new_list,ct)
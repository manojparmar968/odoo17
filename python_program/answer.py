n=[5,2,1,4,3,2,8,4,2,1,2,0]
new_lst = []
count_list = []
c = 0

for i in n:
  if i not in new_lst:
    new_lst.append(i)
    c = n.count(i)
    count_list.append(c)
print(new_lst,count_list)
d = {}
for k in new_lst:
  for v in count_list:
    d[k] = v
    count_list.remove(v)
    break
print(d)

dd = {}
for i in n:
  if i in dd:
    dd[i] += 1
  else:
    dd[i] = 1

print(dd)
"""
1
2 9
3 8 10
4 7 11 14
5 6 12 13 15
"""
n = 5
# for i in range(n):
#     for j in range(i + 1):
#         x = 0
#         for k in range(j):
#             x = x + n - k
#             if j % 2 == 0:
#                 print(x + i - j + 1,end=" ")
#             else:
#                 print(x + n - i,end=" ")
#         print()
# print("\n")

# for i in range(n):
#     for j in range(i + 1):
#         # if j % 2 == 0:
#             print(i - j + 1,end=" ")
        
#     print()

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
n=[5,2,1,4,3,2,8,4,2,1,2,0]

uniq_list = []
c = 0
count = []
for i in n:
    if i not in uniq_list:
        uniq_list.append(i)
        c = n.count(i)
        count.append(c)
print(uniq_list,count)
d= {}
for k in uniq_list:
    for v in count:
        d[k] = v
        count.remove(v)
        break
print(d)
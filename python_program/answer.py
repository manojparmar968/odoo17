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
n = [3,2,1,5,4,6,7,8]
# for i in n:
    # for j in 
# print(sorted(n)[0])
middle = int(len(n)/2)
# print(middle)
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] >= n[j]:
            n[i],n[j] = n[j],n[i]
print(n[0])

# depnds
# total = fields.integer(cpmpute="total_value")
# <field name ="" context="{'':''}"/>
# fields_view_get()

# def total_value(self):
    # ensure_one()
    # for i i
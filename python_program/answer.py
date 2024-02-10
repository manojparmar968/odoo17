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

for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] >= n[j]:
            n[i],n[j] = n[j],n[i]
print(n)
n1 = [3,2,1,5,4,6,7,8]
for x in range(len(n1)):
    for y in range(x+1,len(n1)):
        if n1[x] <= n1[y]:
            n1[x],n1[y] = n1[y],n1[x]
print(n1)
# fields_view_get()


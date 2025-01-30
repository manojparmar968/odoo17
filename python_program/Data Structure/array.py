#  sum is equal to the target.
arr = [2,6,5,8,11]
target = 14

print(len(arr)-1,len(arr))
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"the target value of sum {arr[i]} & {arr[j]}",i,j)


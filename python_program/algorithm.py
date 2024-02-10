# 1. Tree traversal algorithms 
# 2. Sorting algorithms/Sorting Types
    # a. Bubble Sort
def bubble_sort(arr):
    index = len(arr)-1
    for i in range(index):
        for j in range(index - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [32,2,5,3,6,7]
print(bubble_sort(arr))

    # b. Selection Sort
    # c. Insertion Sort
    # d. Merge Sort
    # e. Heap Sort
    # f. Quick Sort
# 3. Searching algorithms
    # a. Binary Search
    # Note- List can be in sorted order.
def binary_search(arr,starting_index,last_index,search_number):
    while(starting_index <= last_index):
        middle_number = (starting_index + last_index)//2
        if search_number > arr[middle_number]:
            starting_index = middle_number + 1
        elif search_number < arr[middle_number]:
            last_index = middle_number - 1
        elif search_number == arr[middle_number]:
            return middle_number
    return -1
arr = [2, 3, 4,5,10,14,20,30,40]
search_number = 20
starting_index = 0
last_index = len(arr)-1
find = binary_search(arr,starting_index,last_index,search_number)
# print(find)

    # b. Linear Search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10,20,80,30,60,50,110,100,130,170]
x = 110
print(linear_search(arr,x))
for i in range(len(arr)):
    if arr[i] == x:
        print(i)

# 4. Graph algorithms
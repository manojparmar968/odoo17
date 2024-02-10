# Sorting Types
# 1. Linear search
arr = [10,20,80,30,60,50,110,100,130,170]
x = 110
for i in range(len(arr)):
    if arr[i] == x:
        print(i)

# def linear_search()

# 2. Binary search
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
print(find)

# 1. Tree traversal algorithms 
# 2. Sorting algorithms
    # a. Bubble Sort
    # b. Selection Sort
    # c. Insertion Sort
    # d. Merge Sort
    # e. Heap Sort
    # f. Quick Sort
# 3. Searching algorithms
    # a. Binary Search
    # b. Linear Search
# 4. Graph algorithms
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort(arr=[3, 1, 2, 4]))

'''
TRACING -

nums = [3, 1, 2, 4]

merge_sort() is called first

if len(arr) <= 1:
false

mid = len(arr) // 2
mid = 4 // 2 -> 2
mid = 2

left = merge_sort(arr[:mid])
arr[mid:] = arr[2:] -> [3, 1]

if len(arr) <= 1
arr = [3, 1]
false

mid = len(arr) // 2
mid = 2 // 2 -> 1
mid = 1

left = merge_sort(arr[:mid])
arr[mid:] = arr[1:] -> [3]

if len(arr) <= 1
arr = [3] -> true
    return arr

left = [3]

right = merge_sort(arr[mid:])
arr[mid:] = arr[1:] = [1]

if len(arr) <= 1
arr = [1] -> true
    return arr

right = [1]

merge(left, right) is called
left = [3]
right = [1]

merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
    0 < 1 and 0 < 1 -> true
        if left[i] <= right[j]:
        left[0] <= right[0] -> 3 <= 1 -> false

        else:
            result.append(right[j])
            result = [1]
            j = j + 1
            j = 1

    while i < len(left) and j < len(right):
    0 < 1 and 1 < 1 -> false

    result.extend(left[i:]) -> left[0:]
    result = [1, 3]

    result.extent(right[j:]) -> right[1:]
    result = [1, 3] (there is nothing to extend)

    return result 
    result = [1, 3]

line number 44 -> last we did was for left. Now we do the same thing for right

right = merge_sort(arr[mid:])
arr = [1, 3, 2, 4]
mid = 2

merge_sort(arr[2:]) -> [2, 4]

if len(arr) <= 1:
arr = [2, 4]
false

mid = len(arr) // 2
mid = 1

left = merge_sort(arr[:mid])
left = merge_sort(arr[:1])
left = [2]

if len(arr) <= 1:
arr = [2] -> true
    return arr

right = merge_sort(arr[mid:])
right = merge_sort(arr[1:])
right = [4]

if len(arr) <= 1:
arr = [4] -> true
    return arr

merge(left, right) is called
left = [2]
right = [4]

merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
    0 < 1 and 0 < 1 -> true
        if left[i] <= right[j]:
        left[0] <= right[0] -> 2 < 4 -> true
            result.append(left[i]) -> left[0]
            result = [2]

            i = i + 1
            i = 1

    while i < len(left) and j < len(right):
    1 < 1 -> false

    result.extend(left[i:]) -> left[1:]
    result = [2] (nothing to extend)
    result.extend(right[j:]) -> right[0:]
    result = [2, 4]

    return result
    result = [2, 4]

again we go to merge(left, right)
left = [1, 3]
right = [2, 4]

merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
    0 < 2 and 0 < 2 -> true
        if left[i] <= right[j]:
        left[0] <= right[0] -> 1 < 2 -> true

            result.append(left[i]) -> left[0]
            result = [1]

            i = i + 1
            i = 1

    while i < len(left) and j < len(right):
    1 < 2 and 0 < 2 -> true
        if left[i] <= right[j]:
        left[1] <= right[0] -> 3 < 2 -> false

        else:
            result.append(right[j]) -> right[0]
            result = [1, 2]

            j = j + 1
            j = 1

    while i < len(left) and j < len(right):
    1 < 2 and 1 < 2 -> true
        if left[i] <= right[j]:
        left[1] <= right[1] -> 3 < 4 -> true
            result.append(left[i]) -> left[1]
            result = [1, 2, 3]

            i = i + 1
            i = 2

    while i < len(left) and j < len(right):
    2 < 2 -> false

    result.extend(left[i:]) -> left[2:]
    result = [1, 2, 3] -> nothing to extend

    result.extend(right[j:]) -> right[1:]
    result = [1, 2, 3, 4]

    return result 

Output = [1, 2, 3, 4]

'''
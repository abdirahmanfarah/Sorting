# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    # if arrA = [4,8,1,5] and arrB = [3,6,9,7.2]
    # Figure out the length of the array
    elements = len(arrA) + len(arrB)
    # declare variable to multiply the length of the array by an empty array
    merged_arr = [0] * elements
    a = 0
    b = 0
    # fill the empty array with the values of the actual arrays
    # loop through the merged_arr and add arrA and arrB together.
    # While merged_arr has a length greather than 1
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# arr = [1, 2, 3]
# arr1 = [4, 5, 6]
# merge(arr, arr1)
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):

    if len(arr) > 1:
        print(arr)
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr
 # TO-DO
    # BASE CASE
    # if len(arr) == 1:
    #     return arr
    # # Divide array in half
    # half = len(arr) // 2
    # # Save each side of the divided array into it's own variable
    # x = arr[:half]
    # y = arr[half:]
    # # keep dividing in half until each element is it's own array.
    # merge_sort(x)
    # merge_sort(y)

    # # sort the array once there are two elements in it
    # # call helper function
    # merge(x, y)


# arr = [5, 3, 1, 6, 7, 9, 4, 2, 8]
# print(merge_sort(arr))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    # Takes one array
    # BUILD WHILE LOOP, manipulate the pointers
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return arr

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    # arr[3,5] arr2[5,6]
    if len(arr) > 1:
        l = merge_in_place(len())

    return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr

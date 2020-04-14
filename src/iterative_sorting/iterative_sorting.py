# TO-DO: Complete the selection_sort() function below
# [5, 7, 8, 3, 9]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Make the current index which is at 0 equal to i
        cur_index = i
        # smallest_index is our temp index which equals to our current index
        smallest_index = cur_index
        # print(arr[smallest_index] + arr[smallest_index])
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        #
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                arr[smallest_index], arr[j] = arr[j], arr[smallest_index]

    # TO-DO: swap
    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# selection_sort(arr1)
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through the array
    # compare first indice to the second indice to see which is bigger
    # if the indice to the right is bigger, swap them

    swap = True

    while swap:
        swap = False
        for j in range(len(arr) - 1):
            # print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(arr1)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

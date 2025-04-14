#Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
#You need to solve this problem without utilizing the built-in sort function.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    return arr

arr1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr2 = [0, 1, 2, 0, 1, 2]

print(bubble_sort(arr1))
print(bubble_sort(arr2))
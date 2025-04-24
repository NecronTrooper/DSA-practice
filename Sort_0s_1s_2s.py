#Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
#You need to solve this problem without utilizing the built-in sort function.
def bubble_sort(arr):     # Doesn't fit by requirement, need optimization
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    return arr

def Dutch_national_flag_algo(arr):  # The Dutch National Flag Algorithm is a sorting algorithm that divides an array into three segments 
                                    # based on three distinct values, often referred to as low, mid, and high. 
                                    # The algorithm efficiently rearranges elements so that all low elements come first, 
                                    # followed by mid elements, and finally, all high elements.
    
    low = 0
    mid = 0
    high = len(arr) - 1 
    
    temp = 0

    while(mid < high):  
        if(arr[mid] == 0):
            low += 1
            

    return arr


arr1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr2 = [0, 1, 2, 0, 1, 2]

print(Dutch_national_flag_algo(arr1))
print(Dutch_national_flag_algo(arr2))




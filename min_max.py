def min_max(arr):
   n = len(arr)
   min_val = float('inf')
   max_val = float('-inf')
   for i in range(n):
      if min_val > arr[i]:
         min_val = arr[i]
      if max_val < arr[i]:
         max_val = arr[i]
   return min_val, max_val

arr_v=[1, 20, 5 , 80, 6]
print(min_max(arr_v))
def k_smallest(arr, a):
   n = len(arr)
   
   for i in range(n):
      min_v = float('inf')
      for j in arr:
         if min_v > j:
            min_v = j
      
      if i == a-1:
         return min_v
      arr.remove(min_v)


array = [9 , 7, 11, 31, 8 ,15]
print(k_smallest(array, 3))
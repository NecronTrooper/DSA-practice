import random

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


def reverse_arr(arr):
    n = len(arr)
    temp_arr = [0] * n
    for i in range(n):
        temp_arr[i] = arr[n-1-i]
    return temp_arr



size = 10  
min_value = 1 
max_value = 100  
random_array = generate_random_array(size, min_value, max_value)
print('random array:')
print(random_array)
print('reversed random array:')
print(reverse_arr(random_array))



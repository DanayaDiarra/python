def bubble_sort(arr):  
    n = len(arr)  
    # Traverse through all elements in the array  
    for i in range(n):  
        # Last i elements are already in place  
        for j in range(0, n - i - 1):  
            # Compare and swap if necessary  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr  

# Testing the sorting function with different lists  
short_list = [64, 34, 25, 12, 22]  
long_list = [64, 34, 25, 12, 22, 11, 90, 53, 75, 88, 9, 1, 3, 7, 100]  

sorted_short_list = bubble_sort(short_list.copy())  
sorted_long_list = bubble_sort(long_list.copy())  

print("Sorted Short List:", sorted_short_list)  
print("Sorted Long List:", sorted_long_list)
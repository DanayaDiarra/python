# smallest.py  
def find_two_smallest(int_list):  
    """Returns the two smallest values from a list of integers."""  
    if len(int_list) < 2:  
        raise ValueError("The list must contain at least two integers.")  
    
    # Initializing variables for the smallest two values  
    min1 = min2 = float('inf')  
    
    for num in int_list:  
        if num < min1:  
            min2 = min1  # Updating the second smallest  
            min1 = num  # Updateing the smallest  
        elif min1 < num < min2:  
            min2 = num  # Updating the second smallest  
    
    return [min1, min2]
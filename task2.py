def is_power(base, number):   
    if base <= 1:  
        return number == 1  # 1 is the power of any number, and bases <= 1 are not valid for powers  
    if number < 1:  
        return False  # No positive number can be a power of another if it's less than 1    
    power = base    
    while power < number:  
        power *= base   
    return power == number  

  
print(is_power(2, 16))         
print(is_power(2, 12))        
print(is_power(10, 100000))    
print(is_power(9, 990))        
print(is_power(2, 0))  
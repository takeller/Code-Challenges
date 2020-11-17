def find_even_index(arr):
    array_length = len(arr)
    for index, int in enumerate(arr): 
        
#     Sum left side 
        if index == 0: 
            left_sum = 0 
        else: 
            left_sum = sum(arr[0:index])
            
#     Sum right side 
        if index == (array_length - 1): 
            right_sum = 0 
        else: 
            right_sum = sum(arr[index + 1:])
         
        if right_sum == left_sum: 
            return index 
    
    return -1
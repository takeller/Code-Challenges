def persistence(num, count = 0):
    if type(num) != int: 
        return "Error: Input must be an integer"

    if num < 10 and num > -1: 
        return count 

    num = str(abs(num))
    result = 1

    for digit in num: 
        result *= int(digit)
    
    count += 1
    return persistence(result, count)
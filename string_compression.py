# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters. 


def compress(string): 
    given_string = string 
    given_string_length = len(given_string)
    compressed_string = ''
    previous_index = None
    count = 0

    for index, character in enumerate(string): 
        if index == 0: 
            count += 1
            previous_index = index 
            continue

        if string[previous_index] == string[index] and index == (given_string_length - 1):
            count += 1 
            compressed_string = compressed_string + string[previous_index] + str(count)
        elif index == (given_string_length - 1):
            compressed_string = compressed_string + string[previous_index] + str(count)
            compressed_string = compressed_string + string[index] + '1'
        elif string[previous_index] == string[index]: 
            count += 1 
            previous_index = index 
        else: 
            compressed_string = compressed_string + string[previous_index] + str(count)
            previous_index = index
            count = 1

    # Compare compressed with original 
    if len(given_string) <= len(compressed_string): 
        return given_string
    else: 
        return compressed_string 


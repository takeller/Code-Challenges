# def how_many(sentence):
#      words = sentence.split()
#      for word_tuple in enumerate(words): 
#         index = word_tuple[0]
#         word = word_tuple[1]
#         if validity_check(word) == False: 
#             words.pop(index)
#      print(words)
#      return len(words)
def how_many(sentence):
     words = sentence.split()
     for word in words[:]: 
        if validity_check(word) == False: 
            words.remove(word)
     print(words)
     return len(words)
"""
Checks for validity of the substring. 
    - Numeric strings are not valid
    - Punctuation without letters is not valid
    - Any characters outside of 'a-z', 'A-Z', '.', ',', '?', '!' are not valid
"""
def validity_check(string):
    valid_letters = dict.fromkeys('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', True)
    valid_punctuation = dict.fromkeys('!,.?-', True)
    chars = []
    chars[:] = string
    # import pdb; pdb.set_trace()
    for char in chars: 
        if char not in valid_letters and char not in valid_punctuation:
            return False
        
        # Remove punctuation from the substring
        if char in valid_punctuation:
            chars.remove(char)

    # If the substring only contained punctuation [.,!?], then length should be zero, and the substring invalid
    if len(chars) == 0: 
        return False

    return True 
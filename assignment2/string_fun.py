# Author: Shawn Yat Sin
# ID: 261052225

def remove_substring_from_string(s, substr):
    ''' (str, str) -> str
    Creates a new string from the original string s by removing all instances of substr, if any.
    
    >>> remove_substring_from_string("life has no meaning.", ' no')
    'life has meaning.'
    
    >>> remove_substring_from_string('abracadabra', 'a')
    'brcdbr'
    
    >>> remove_substring_from_string('math is complex', 'z')
    'math is complex'
    
    >>> remove_substring_from_string('ccccccc', 'cc')
    'c'
    
    '''

    removal_list = []
    
    for i in range(len(s)):
        if i not in removal_list: # to not check the same character twice
            if s[i:i+len(substr)] == substr: # if the substr is found in s
                for index in range(i, i + len(substr)): # append each index that corresponds to a char in substr to the removal list
                    removal_list.append(index)
    
    new_string = ''
    for j in range(len(s)): 
        if j not in removal_list: # add each character not in the removal list to the new_string
            new_string += s[j]
                
    return new_string


def get_nth_comma_in_string(s, n):
    '''(str, int) -> int
    Returns the index of the nth comma in the string s.
    
    >>> get_nth_comma_in_string("oh, i, keep, talking, in, commas, sorry, about, that", 0)
    2
    
    >>> get_nth_comma_in_string("if I could see ',,,,', then I could be happy", 4)
    21
    
    >>> get_nth_comma_in_string("if I could see ',,,,', then I could be happy", 5)
    -1
    
    >>> get_nth_comma_in_string("if, to, without, is, just", 5)
    -1
    
    '''
    nb_of_commas = 0 
    for i in range(len(s)): #  counts number of commas
        if s[i] == ',':
            nb_of_commas += 1
            
    if n < 0 or n >= nb_of_commas: # returns -1 if n is not within the number of commas
        return -1
    
    comma_index = s.find(',')   # index of first comma n=0
    for j in range(n): # repeats the comma search n number of times 
        comma_index = s.find(',', comma_index + 1, len(s))
        # finds the index of the next comma by excluding the range of the previous one by adding 1
        # searches next comma from [previous comma_index + 1: len(s)]
        
    return comma_index


def get_nth_word_from_string(s, n):
    ''' (str, int) -> str
    Returns the nth comma separated substring in string s.
     
    >>> get_nth_word_from_string("dreary, pondered, weak, weary", 0)
    'dreary'
    
    >>> get_nth_word_from_string("fall, stand, break, peace", 1)
    'stand'
    
    >>> get_nth_word_from_string("fall, stand, break, peace, shake", 2)
    'break'
    
    >>> get_nth_word_from_string("fall", 0)
    'fall'
    
    >>> get_nth_word_from_string("fall, stand, break, peace", 4)
    ''
    
    '''
    index_of_commas = [] # takes the indexes of the commas in the string s
    nb_of_commas = 0
    for i in range(len(s)): 
        if s[i] == ',':
            index_of_commas.append(i)   # adds the index of the comma into index_of_commas
            nb_of_commas += 1 # counts the number of commas
            
    if n > nb_of_commas or n < 0: # checks if n is valid
        return ''
    
    elif n == 0: # for first substring in string s
        if nb_of_commas == 0: # if there is no comma
            return s
        else:
            return s[:index_of_commas[n]] # s[: first comma]
    
    elif n > 0 and n <= nb_of_commas - 1: # for any substring in between first and last substring
        return s[index_of_commas[n-1]+2:index_of_commas[n]]
        # [previous comma + 2 to skip the comma and space: next comma]
    
    elif n == nb_of_commas: # for last substring 
        return s[index_of_commas[n-1]+2:] # [before last comma + 2:]
    
def sum_numbers(my_list):
    ''' (list) -> int
    Takes a list of numbers and returns the sum.
    
    >>> sum_numbers([44,30,75,18,72])
    239
    
    >>> sum_numbers([3.5, 34, 4, 5])
    46.5
    
    >>> sum_numbers([0, 4, 5, -322])
    -313
    
    '''
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i]
        
    return sum
    
def insert_substrings_into_string(s, substrs):
    ''' (str, str) -> str
    Returns a new string from the original string s where all the placeholder sequences in s are replaced by substrings in substrs.
    
    >>> insert_substrings_into_string("Once upon a midnight %0, while I %1, %2 and %3", \
    "dreary, pondered, weak, weary")
    'Once upon a midnight dreary, while I pondered, weak and weary'
    
    >>> insert_substrings_into_string("My favorite %1 is %1!!!", "programming language, Python")
    'My favorite Python is Python!!!'
    
    >>> insert_substrings_into_string("My favorite %10 is %1!!!", "programming language, Python")
    'My favorite %10 is Python!!!'
    
    >>> insert_substrings_into_string("My favorite % is %1!!!", "programming language, Python")
    'My favorite % is Python!!!'
    
    '''
    new_string = s
    count = 0
    length_substrs = []
    list_nb_digits = []
   
    for i in range(len(s)): 
        if s[i] == '%':
            
# 1. Input validation 
            if i == len(s) - 1: # if % is the last character in string, return original string
                break
            
# 2. Determining placeholder number
            placeholder_nb = ''
            nb_digits = 1 # counter for number of digits in placeholder_nb, starts at 1 to count % character
            
            while s[i + nb_digits].isdecimal(): # checks for numbers after the placeholder symbol
                placeholder_nb += s[i + nb_digits]   # add the digits as strings to string placeholder_nb
                nb_digits += 1
                
                if i + nb_digits == len(s): # if the index is the last character in the string, prevent IndexError
                    break
                
# 3. Determine the substring that will be inserted                
            nb_of_commas = 0
            for j in range(len(substrs)): 
                if substrs[j] == ',':
                    nb_of_commas += 1 # counts the number of commas
            
            if nb_digits == 1: # if there is no placeholder_nb, insert symbol as it is
                substr_desired = '%'
            
            elif int(placeholder_nb) > nb_of_commas: # if placeholder_nb is not a valid index
                substr_desired = '%'+ placeholder_nb # placeholder sequence will be added in new_string
                
            else:    
                substr_desired = get_nth_word_from_string(substrs, int(placeholder_nb))
                # will get the word in substrs at index of placeholder_nb
                
            length_substrs.append(len(substr_desired)) # length of susbtr_desired is added to a list length_substrs
            list_nb_digits.append(nb_digits) # the number of digits taken by the placeholder_nb added to a list
            first_half_shift = sum_numbers(length_substrs[0:count]) - sum_numbers(list_nb_digits[0:count])
            # first_half_shift represents the shift required to find the range [0:%]
            # it adds the lengths of the substrs that have been inserted - the lengths of the placeholder sequences removed
            second_half_shift = sum_numbers(length_substrs[0:count]) - sum_numbers(list_nb_digits[0:count]) + nb_digits
            # second_half_shift represents the shift required to find the range [last digit of placeholder sequence + 1:]
            new_string = new_string[0:i + first_half_shift] + substr_desired + new_string[i + second_half_shift:]
            count += 1 # used to know number of times strings have been replaced
     
    return new_string

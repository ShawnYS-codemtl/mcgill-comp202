# Author: Shawn Yat Sin
# ID: 261052225

import random

def do_op_for_numbers(op, num1, num2):
    ''' (str, int, int) -> int
    Returns the result of the operation in string op applied to num1 and num2
    
    >>> do_op_for_numbers('-', 1, 2)
    -1
    
    >>> do_op_for_numbers('/', 17, 4)
    4
    
    >>> do_op_for_numbers('^', 8, 2)
    64
    
    >>> do_op_for_numbers('/', 8, 0)
    0
    
    '''
    if op == '+':
        result = num1 + num2 # addition
        
    elif op == '-':
        result = num1 - num2 # subtraction
        
    elif op == 'x':
        result = num1 * num2 # multiplication
        
    elif op == '/':
        if num2 == 0:
            result = 0 # returns 0 if division by 0
        else:   
            result = num1 // num2 # floor division
            
    elif op == '^':
        result = num1 ** num2 # power
        
    return result

def remove_from_list(my_list, indices):
    ''' (list, list) -> list
    Returns a new list created by removing elements from my_list at indices given by integers in the list indices.
    
    >>> remove_from_list(['The', 'quick', 'brown', 'fox'], [3, 0])
    ['quick', 'brown']
    
    >>> remove_from_list([2, 5, 'dog', 'polar bear'], [1, 2])
    [2, 'polar bear']
    
    >>> remove_from_list(['The', 'quick', 'brown', 'fox'], [0, 3])
    ['quick', 'brown']
    
    >>> remove_from_list(['The', 'quick', 'The', 'fox'], [0, 1, 2])
    ['fox']
    
    >>> remove_from_list(['The', 'quick', 'The', 'fox'], [0, 1, 2, 4])
    ['fox']
    
    '''
    new_list = []
    my_list_copy = []
    nb_elements = 0
    for ele in my_list:
        my_list_copy.append(ele) # copies each element of my_list into my_list_copy
        nb_elements += 1 # counts number of elements
                
    for j in range(len(my_list_copy)):
        if j not in indices:
            new_list.append(my_list_copy[j]) # appends elements whose indices are not in the list indices to new_list
        
    return new_list

def find_last(my_list, x):
    ''' (list, x) -> int
    Returns the index of the last element of my_list which is equal to x, if it cannot be found, returns None instead.
    
    >>> find_last(['a', 'b', 'b', 'a'], 'b')
    2
    
    >>> find_last(['dog', 'cat', 'cat', 5, 'dog'], 'dog')
    4
    
    >>> find_last([1, 2, 3, 3, 2, 1, 2, 4, 5], 1)
    5
    
    >>> ind = find_last(['a', 'b', 'b', 'a'], 'ab')
    >>> print(ind)
    None
    
    '''
    common_list = []
    for i in range(len(my_list)):
        if my_list[i] == x: 
            common_list.append(i) # appends the index of elements in my_list equal to x to common_list 
            
    if common_list == []: # if there are no elements in common_list
        return None

    return common_list[len(common_list) - 1] # returns last element in common_list

def find_first(my_list, x):
    ''' (list, x) -> int
    Returns the index of the first element of my_list which is equal to x; if it cannot be found, returns None instead.
    
    >>> find_first(['a', 'b', 'b', 'a'], 'b')
    1
    
    >>> find_first(['a', 'b', 'b', 'a'], 'a')
    0
    
    >>> ind = find_first([1, 2, 3, 4, 5], 21)
    >>> print(ind)
    None
    
    >>> find_first(['a', 'b', 'b', 'a', 'd'], 'd')
    4
    
    '''
    if x in my_list:
        return my_list.index(x) # returns the index of the first element in my_list
           
    else:
        return None

def generate_num_digits(pct_per_digit):
    ''' (float) -> int
    Generates a random percentage between 0 and 1. Increase the integer to be returned by 1 until that percentage is greater than or
    equal to pct_per_digit. Returns the integer.
    
    >>> random.seed(9001)
    >>> generate_num_digits(0.5)
    3
    
    >>> generate_num_digits(0)
    1
    
    >>> generate_num_digits(1)
    0
    
    >>> generate_num_digits(-2)
    0
    
    '''
    
    nb_digits = 1
    if pct_per_digit >= 1 or pct_per_digit < 0: # if percentage is not valid
        nb_digits = 0 # returns an arbitrary 0
    else:
        while random.random() < pct_per_digit: # generates a random float between 1 and 0 and continues loop if less than percentage
            nb_digits += 1
    return nb_digits

def generate_number(pct_per_digit):
    ''' (float) -> int
    Returns a random number with length determined by previous function.
    
    >>> random.seed(1337)
    >>> generate_number(0)
    9
    
    >>> random.seed(9002)
    >>> generate_number(0.5)
    42009
    
    >>> test = generate_number(1)
    >>> print(test)
    None
    
    >>> test = generate_number(-2)
    >>> print(test)
    None
    
    '''
    num_digits = generate_num_digits(pct_per_digit) # randomly assigns an int to num_digits
    if num_digits == 0: # if pct_per_digit is invalid
        return None
    min_random_nb = 10 ** (num_digits - 1) # minimum number possible defined by instructions
    max_random_nb = 10 ** num_digits - 1 # maximum number possible defined by instructions
    return random.randint(min_random_nb, max_random_nb) # returns random int between min and max

def check_equivalency(tokens):
    ''' (list) -> bool
    Returns True if tokens contains three elements, the second element is an equals sign, and the first and third elements are equal
    to each other. Returns False otherwise.
    
    >>> check_equivalency([4, '=', 4])
    True
    
    >>> check_equivalency([4, '=', 5])
    False
    
    >>> check_equivalency(['dog', '=', 'dog'])
    True
    
    >>> check_equivalency([1, 2, 3])
    False
    '''
    nb_elements = 0
    for i in range(len(tokens)): # counts the nb of tokens in the list
        nb_elements += 1
        
    return nb_elements == 3 and tokens[1] == '=' and tokens[0] == tokens[2] 
        





   

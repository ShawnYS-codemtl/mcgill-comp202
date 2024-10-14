# Author: Shawn Yat Sin
# ID: 261052225

import random as r
import blackout_utils as b

OPERATIONS = ['^', 'x', '/', '+', '-']

def get_tokens_from_equation(line):
    ''' (str) -> list
    Translates the string line into a list of tokens. A token is a single non-negative number (of any length) or a single
    mathematical symbol.
    
    >>> get_tokens_from_equation('6-5=15^4/2')
    [6, '-', 5, '=', 15, '^', 4, '/', 2]
    
    >>> get_tokens_from_equation('6-5a=15^4/b2=')
    [6, '-', 5, '=', 15, '^', 4, '/', 2, '=']
    
    >>> get_tokens_from_equation('-3dxs4-5953(')
    ['-', 3, 'x', 4, '-', 5953, '(']
    
    '''
    token_list =[]
    i = 0
    while i < len(line):
         
        if line[i].isdecimal(): # if token is decimal
            token_nb = '' # resets the number
            
            while line[i].isdecimal(): # checks for consecutive digits
                token_nb += line[i] # adds digits to string token_nb
                i += 1
                if i == len(line): # prevents IndexError
                    break
            token_list.append(int(token_nb)) # appends token_nb to token_list
        
        elif line[i] in ['+','-','x','/','=','^','(',')']: # if token is an operation, adds it directly to list
            token_list.append(line[i])
            i += 1
            
        else:
            i += 1 # skips over non valid characters in string line
            
    return token_list
        
def process_operations(ops, tokens):
    ''' (list, list) -> list
    Returns a new list with the result of operations from list ops on the tokens in list tokens.
    
    >>> process_operations(['x'], [5, 'x', 7, '+', 2])
    [35, '+', 2]
    
    >>> process_operations(['x', '^'], [2, 'x', 3, '^', 2, 'x', 2]) # multiple operations
    [72]
    
    >>> process_operations(['x', '^'], [2, 'x', 3, 'x']) # operation at end of list
    [2, 'x', 3, 'x']
    
    >>> process_operations(['x', '^'], ['x', 3, '^', 2, 'x', 2]) # operation at start of list
    ['x', 3, '^', 2, 'x', 2]
    
    >>> process_operations(['x'], [3,'x',4, 3]) # two consecutive numbers
    [3, 'x', 4, 3]
    
    >>> process_operations(['x'], [3, 'x', 'x', 5]) # two operations in a row
    [3, 'x', 'x', 5]
    
    '''
# 1. Copy tokens into tokens_copy
    tokens_copy = []
    for ele in tokens:
        tokens_copy.append(ele)
    
# 2. Check for invalid inputs
    if type(tokens_copy[0])!= int or type(tokens_copy[len(tokens_copy)-1]) != int: # if operation at beginning or end of list
        return tokens
    
    i = 0    
    while i < len(tokens_copy) - 1:
        if type(tokens_copy[i]) == int and type(tokens_copy[i+1]) == int: # if two numbers in a row
            return tokens
        
# 3. Process operation   
        if type(tokens_copy[i]) == int and i < len(tokens_copy) - 2: # if token is an int and there are at least 2 tokens following
            if tokens_copy[i+1] in ops and type(tokens_copy[i+2]) == int: # if next token in ops and the following is an int
                new_token = b.do_op_for_numbers(tokens_copy[i+1], tokens_copy[i], tokens_copy[i+2]) # does operation
                tokens_copy[i:i+3] = [new_token] # replaces the three tokens involved with the result of the operation
                i -= 1 # keeps the counter the same to check for operations involving the new token
            i += 1
                
        else:
            i += 1 # skips to next token
                
    return tokens_copy

def calculate(tokens):
    ''' (list) -> list
    Evaluates both sides of the equality in list tokens and returns a list of three tokens: the result of the left-hand side (integer), the equals sign
    (string), and the result of the right-hand side (integer).
    
    >>> calculate([5, 'x', '(', 4, '+', 2, ')', '=', 49]) # evaluates operation in parenthesis first
    [30, '=', 49]
    
    >>> calculate([3, '^', 2, '+', '(', 2, 'x', 6, '^',2, ')', '=', 7]) # respects order of operations within parentheses and out
    [81, '=', 7]
    
    >>> calculate([3, 'x', '(',2, 'x','(', 4, '+', 3, '^', '(', 2, '+', 1, ')', ')', ')', '=', 1]) # multiple parentheses
    [186, '=', 1]
    
    >>> calculate([3, '^', 2, '+', '(', 3, '-', 4, ')', '+', '-', 2, '=', 2, 'x', 2]) # for two operations in a row
    [3, '^', 2, '+', '(', 3, '-', 4, ')', '+', '-', 2, '=', 2, 'x', 2]
    
    >>> calculate(['(','(','(',1, ')', ')', ')', '=', 2]
    [1, '=', 2]
    
    '''
# 1. Copies each element of tokens into tokens_copy
    tokens_copy = []
    for ele in tokens:
        tokens_copy.append(ele)
        
# 2. Checks for invalid inputs   
    if '=' not in tokens_copy: # if there is no equality
        return tokens
    
    if tokens_copy[0] in OPERATIONS or tokens_copy[len(tokens_copy)-1] in OPERATIONS: # if operation is at beginning or end of list, return tokens
        return tokens
    i = 0
    nb_open_par = 0
    nb_close_par = 0
    while i < len(tokens_copy) - 1:
        if type(tokens_copy[i]) == int and type(tokens_copy[i+1]) == int: # if two numbers in a row
            return tokens
        
        if tokens_copy[i] in OPERATIONS and tokens_copy[i+1] in OPERATIONS: # if two operations in a row
            return tokens
        
        if tokens_copy[i] == '(':
            if tokens_copy[i+1] in OPERATIONS: # ex: (+ for operations following opening parenthesis
                return tokens
            nb_open_par += 1
            
        if tokens_copy[i] == ')':
            if tokens_copy[i-1] in OPERATIONS: # ex: +) for operations right before closing parenthesis
                return tokens
            nb_close_par += 1
        i += 1
            
    if nb_open_par != nb_close_par: # if parentheses are not closed
        return tokens
    
# 3. Operations in parentheses
    while '(' and ')' in tokens_copy: # loops until there are no more parentheses
        open_parenthesis = b.find_last(tokens_copy, '(') # finds most inner open_parenthesis
        close_parenthesis = b.find_first(tokens_copy, ')') # finds most inner closed_parenthesis
        
        parenthesis_evaluation = [] # for operations in parentheses, resets value for each set of parentheses
        
        parenthesis_evaluation = process_operations(['^'], tokens_copy[open_parenthesis + 1: close_parenthesis]) # applies exponent op
        parenthesis_evaluation = process_operations(['x', '/'], parenthesis_evaluation) # applies multiplication and division
        parenthesis_evaluation = process_operations(['+', '-'], parenthesis_evaluation) # applies  addition and subtraction
        
        tokens_copy[open_parenthesis: close_parenthesis + 1] = parenthesis_evaluation # replaces everything within parentheses, parentheses included
    
# 4. Operations outside parentheses
    equality = process_operations(['^'], tokens_copy) # applies order of operations for tokens outside parentheses
    equality = process_operations(['x', '/'], equality)
    equality = process_operations(['+', '-'], equality)
    
    return equality

def brute_force_blackout(line):
    ''' (str) -> list
    Continuously tries to remove two different characters (digits or operations, except the equals sign) from the original string line
    until the equality holds in the resulting string. If one can be found, then returns the equation (with the two characters removed) as
    a list of tokens.
    
    >>> brute_force_blackout('6-5=15^4/2')
    [6, '-', 5, '=', 1, '^', 42]
    
    >>> brute_force_blackout('288/24x6=18x13x8')
    [288, '/', 4, 'x', 6, '=', 18, 'x', 3, 'x', 8]
    
    >>> brute_force_blackout('16-5x8=0-354^1')
    [6, '-', 5, 'x', 8, '=', 0, '-', 34, '^', 1]
    
    >>> brute_force_blackout('4^8=2-3')
    
    '''
# 1. Convert string line to a list of tokens
    tokens = get_tokens_from_equation(line) 
    ele = 0
    
# 2. Checks for token numbers with more than 1 digit and separates the individual digits of that number  
    while ele < len(tokens):
        string_digits = []
        if len(str(tokens[ele])) > 1: # for numbers with more than 1 digit
            str_conversion = str(tokens[ele]) # convert it to a string
            for digits in range(len(str_conversion)):
                string_digits.append(int(str_conversion[digits])) # append the characters of that string as int to a list string_digits
                
            tokens[ele:ele+1] = string_digits # replace the initial token number by the list
            ele += 1 
        else:
            ele += 1
            
# 3. Removes tokens until an equality holds, returns None otherwise
# 3.1 Create a list indices for the remove_from_list function to take as input that updates itself
    indices = [] # list of two indexes i and j such that i != j
    i = 0
    while i < len(tokens):
        j = i + 1
        while j < len(tokens): # loop through all of j for each i
            indices = []
            indices.append(i)
            indices.append(j)
            tokens_with_holes = b.remove_from_list(tokens, indices) # removes tokens at the position of i and j
            k = 0
            
# 3.2 Checks for consecutive integer tokens and combines them         
            while k < len(tokens_with_holes) - 1:
                if str(tokens_with_holes[k]).isdecimal() and str(tokens_with_holes[k+1]).isdecimal(): # if token is decimal
                    position_of_token_nb = k # to remember position of first digit
                    token_nb = '' # resets the number
            
                    while str(tokens_with_holes[k]).isdecimal(): # checks for consecutive digits
                        token_nb += str(tokens_with_holes[k]) # adds digits to string token_nb
                        k += 1
                        if k == len(tokens_with_holes): # prevents IndexError
                            break
                
                    tokens_with_holes[position_of_token_nb:k] = [int(token_nb)] # appends token_nb to tokens_with_holes list at
                else:                                                           # position of first digit up to last digit 
                    k += 1
                    
# 3.3 Calculates the updated tokens_with_holes and returns it if the equality holds. Otherwise, returns None.                 
            equality = calculate(tokens_with_holes) 
            
            if b.check_equivalency(equality): # if equality holds
                return tokens_with_holes
            else:
                j += 1     
        i += 1 # once all indices of j have been checked, starts next i
    return None # if tokens_with_holes was not returned after all possible indices of i and j

def create_equation(n, pct_per_digit):
    ''' (odd int, float [0,1[) -> list
    Returns a randomly-created mathematical equation as a list of tokens. The list should be of length n. The second input determines
    the chance that a number in the equation will have more than one digit.
    
    >>> r.seed(765)
    >>> create_equation(11, 0.7)
    [2585, '=', 16, '-', 1, '/', 79431, '+', 945, '^', 2]
    
    >>> r.seed(788)
    >>> create_equation(9, 0.5)
    [1, '/', 27, '=', 5020, '+', 4, '+', 2]
    
    >>> r.seed(789)
    >>> create_equation(9, 0.2)
    [1, '+', 77, '=', 4, '-', 5, '/', 6]
    
    >>> r.seed(789)
    >>> create_equation(1, 0.3)
    [1, '=', 77]
  
    '''
    i = 0
    equation = []
    odd_indices = []
    
# 1. Since one number is not an equation, push to smallest equation possible with n == 3
    if n == 1:
        n = 3
        
# 2. Randomly generate a number for even indices and an operation for odd indices and append them to equation one at a time 
    while i < n: # loops to have n elements in equation at the end
        if i % 2 == 0: # if i is even
            number = b.generate_number(pct_per_digit) # generates nb to be appended
            equation.append(number)
            i += 1
            
        elif i % 2 == 1: # if i is odd
            index_ops = r.randint(0, 4) # randomly returns an int for an index in OPERATIONS
            equation.append(OPERATIONS[index_ops]) # appends the element in OPERATIONS at index_ops
            odd_indices.append(i) # adds the odd index to a list odd_indices
            i += 1
            
# 3. Randomly replace an operation in equation by equals sign           
    equals_sign_index = r.randint(0, n-1) # returns a random int between 0 and last possible index in equation
    while equals_sign_index not in odd_indices: # while the random index does not correspond to an operation in equation (odd nb)
        equals_sign_index = r.randint(0, n-1)
        
    equation[equals_sign_index: equals_sign_index+1] = '=' # replace the value at valid equals_sign_index by '='
    
    return equation

def find_solvable_blackout_equation(num_tries, n ,pct_per_digit):
    ''' ((+)int, odd int, float [0,1[) -> list
    Randomly creates and returns a solvable Blackout Math equation of length n and with each number having pct_per_digit chance to have
    more than one digit. If such an equation cannot be generated after the given number of tries, then return None instead.
    
    >>> find_solvable_blackout_equation(1000, 7, 0.4)
    Solved equation:  [80, '/', 16, '=', 5]
    [2, '+', 80, '/', 16, '=', 5]
    
    >>> find_solvable_blackout_equation(1000, 9, 0.6)
    Solved equation:  [5, '=', 1, '+', 4, '/', 5, '^', 0]
    [5, '=', 1, '+', 4, '/', 5, '^', 720]
    
    >>> find_solvable_blackout_equation(1000, 7, 0.6)
    Solved equation:  [0, '=', 9, '/', 8, '/', 5]
    [90, '=', 69, '/', 8, '/', 5]
    
    '''
# 1. Create a random equation of length n
    for tries in range(num_tries):
        equation = create_equation(n, pct_per_digit)
        
# 2. Create a copy of the original equation
        og_equation = []
        for token in equation:
            og_equation.append(token)
        
        
# 2. Checks for token numbers with more than 1 digit and separates the individual digits of that number
        ele = 0
        while ele < len(equation):
            string_digits = []
            if len(str(equation[ele])) > 1: # for numbers with more than 1 digit
                str_conversion = str(equation[ele]) # convert it to a string
                for digits in range(len(str_conversion)):
                    string_digits.append(int(str_conversion[digits])) # append the characters of that string as int to a list string_digits
                    
                equation[ele:ele+1] = string_digits # replace the initial token number by the list
                ele += 1 
            else:
                ele += 1
            
# 3. Removes tokens until an equality holds
# 3.1 Create a list indices for the remove_from_list function to take as input that updates itself
        indices = [] # list of two indexes i and j such that i != j
        i = 0
        while i < len(equation):
            j = i + 1
            while j < len(equation): # loop through all of j for each i
                indices = []
                indices.append(i)
                indices.append(j)
                tokens_with_holes = b.remove_from_list(equation, indices) # removes tokens at the position of i and j
                k = 0
            
# 3.2 Checks for consecutive integer tokens and combines them         
                while k < len(tokens_with_holes) - 1:
                    if str(tokens_with_holes[k]).isdecimal() and str(tokens_with_holes[k+1]).isdecimal(): # if token is decimal
                        position_of_token_nb = k # to remember position of first digit
                        token_nb = '' # resets the number
                
                        while str(tokens_with_holes[k]).isdecimal(): # checks for consecutive digits
                            token_nb += str(tokens_with_holes[k]) # adds digits to string token_nb
                            k += 1
                            if k == len(tokens_with_holes): # prevents IndexError
                                break
                    
                        tokens_with_holes[position_of_token_nb:k] = [int(token_nb)] # appends token_nb to tokens_with_holes list at
                    else:                                                           # position of first digit up to last digit 
                        k += 1
                    
# 3.3 Calculates the updated tokens_with_holes and returns it if the equality holds. Otherwise, returns None.                 
                equality = calculate(tokens_with_holes) 
                
                if b.check_equivalency(equality): # if equality holds
                    return og_equation
                    
                else:
                    j += 1     
            i += 1 # once all indices of j have been checked, starts next i
            
    return None # if tokens_with_holes was not returned after num_tries

           
def menu():
    ''' (NoneType) -> None
    Prints two options available ans asks user to select an option. Calls the appropriate function and prints the return value with an
    appropriate message.
    
    >>> menu()
    Welcome to Blackout Math!
    Please choose from the following:
    1 Solve equation
    2 Create equation
    Your choice: 1
    Please enter the equation without spaces: 5=1+4/5^720
    Solution found: [5, '=', 1, '+', 4, '/', 5, '^', 0]
    Have a nice day!
    
    >>> menu()
    Welcome to Blackout Math!
    Please choose from the following:
    1 Solve equation
    2 Create equation
    Your choice: 2
    Enter number of tries: 1000
    Enter length: 7
    Enter % of additional digit: 0
    Solved equation:  [2, '=', 2, '/', 1]
    Equation: [6, 'x', 2, '=', 2, '/', 1]
    Have a nice day!
    
    >>> menu()
    Welcome to Blackout Math!
    Please choose from the following:
    1 Solve equation
    2 Create equation
    Your choice: 1
    Please enter the equation without spaces: 34^9-12=214/34
    No solution found.
    Have a nice day!
    
    >>> menu()
    Welcome to Blackout Math!
    Please choose from the following:
    1 Solve equation
    2 Create equation
    Your choice: 2
    Enter number of tries: 5
    Enter length: 7
    Enter % of additional digit: 0.4
    No equation could be generated with the given inputs.
    Have a nice day!
    
    '''
    
    print("Welcome to Blackout Math!\n"+"Please choose from the following:")
    print("1 Solve equation")
    print("2 Create equation")
    choice = int(input("Your choice: "))
    
    if choice not in [1,2]:
        print("Invalid Choice")
        
    elif choice == 1:
        equation = input("Please enter the equation without spaces: ")
        solved_equation = brute_force_blackout(equation) # solves the equation
        if type(solved_equation) == list: # if there is an equality, meaning a list was returned 
            print("Solution found:", solved_equation)
        else:
            print("No solution found.")
            
    elif choice == 2:
        num_tries = int(input("Enter number of tries: "))
        length = int(input("Enter length: "))
        pct_per_digit = float(input("Enter % of additional digit: "))
        created_equation = find_solvable_blackout_equation(num_tries, length, pct_per_digit) # creates an equation with the inputs
        if type(created_equation) == list: # if there is a solvable equation within the number of tries
            print("Equation:", created_equation)
        else:
            print("No equation could be generated with the given inputs.")
            
    print("Have a nice day!")
        
                     
    
        
            
    



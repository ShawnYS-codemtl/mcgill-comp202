# Author: Shawn Yat Sin
# ID: 261052225
# Question 2: Create a Markov Model of order k that can be used to generate text.

import doctest
import random

def get_grams(text, k):
    ''' (str, int) -> dict
    Returns a dictionary of k-grams, using the input string text and the given positive integer k.
    
    >>> get_grams('gagggagaggcgagaaa', 2)
    {'ga': {'g': 4, 'a': 1}, 'ag': {'g': 2, 'a': 2}, 'gg': {'g': 1, 'a': 1, 'c': 1}, 'gc': {'g': 1}, 'cg': {'a': 1}, 'aa': {'a': 1}}
    
    >>> get_grams("She sells sea shells by the sea shore.", 1)
    {'S': {'h': 1}, 'h': {'e': 3, 'o': 1}, 'e': {' ': 2, 'l': 2, 'a': 2, '.': 1}, ' ': {'s': 5, 'b': 1, 't': 1}, 's': {'e': 3, ' ': 2, 'h': 2}, 'l': {'l': 2, 's': 2}, 'a': {' ': 2}, 'b': {'y': 1}, 'y': {' ': 1}, 't': {'h': 1}, 'o': {'r': 1}, 'r': {'e': 1}}
    
    >>> get_grams("two plus two equals four.", 3)
    {'two': {' ': 2}, 'wo ': {'p': 1, 'e': 1}, 'o p': {'l': 1}, ' pl': {'u': 1}, 'plu': {'s': 1}, 'lus': {' ': 1}, 'us ': {'t': 1}, 's t': {'w': 1}, ' tw': {'o': 1}, 'o e': {'q': 1}, ' eq': {'u': 1}, 'equ': {'a': 1}, 'qua': {'l': 1}, 'ual': {'s': 1}, 'als': {' ': 1}, 'ls ': {'f': 1}, 's f': {'o': 1}, ' fo': {'u': 1}, 'fou': {'r': 1}, 'our': {'.': 1}}
    
    >>> get_grams('gagggagaggcgagaaa', 0)
    {'': {'g': 9, 'a': 7, 'c': 1}}
    
    >>> get_grams('gag', 4)
    {}
    '''
    grams_dict = {}
    for i in range(len(text)-k): # range prevents IndexError by ignoring last k characters
        if text[i:i+k] not in grams_dict: # if the substring of length k is not in grams_dict
            grams_dict[text[i:i+k]] = [i+k] # create a key-value pair in grams_dict with the substring as key
                                            # store index of the following character as a list for the value
        elif text[i:i+k] in grams_dict: # if key already exists in grams_dict
            grams_dict[text[i:i+k]] += [i+k] # add index of the following character to the list at that key
            
    for k_gram in grams_dict: # for each k-gram in grams_dict
        sub_dict = {} # resets the inner dictionary
        for index in grams_dict[k_gram]: # for each index stored in the list at the k-gram key        
            if text[index] not in sub_dict: # if the character following the k-gram is not a key in sub_dict
                sub_dict[text[index]] = 1 # creates a key_value pair for that character in sub_dict that has value 1
            else:
                sub_dict[text[index]] += 1 # adds subsequent occurences to the counter at corresponding key
                
        grams_dict[k_gram] = sub_dict # adds the sub_dict as a value to the k-gram key in grams_dict
                                      # replaces the index list for each k-gram
        
    return grams_dict

def combine_grams(grams1, grams2):
    ''' (dict, dict) -> dict
    Combines two k-gram dictionaries and returns the new combined dictionary.
    
    >>> combine_grams({'a': {'b': 3, 'c': 9}, 'b': {'a': 10}}, {'b': {'a': 5, 'c': 5}, 'c': {'d': 4}})
    {'a': {'b': 3, 'c': 9}, 'b': {'a': 15, 'c': 5}, 'c': {'d': 4}}
    
    >>> combine_grams({'a': {'b': 3, 'c': 9}}, {'c': {'d': 4}})
    {'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}
    
    >>> combine_grams({'a': {'dog': 4, 'cat': 3}, 'b': {'dog': 6}, 'c': {'cat': 1}}, {'a': {'dog': 3, 'rat': 8}, 'd': {'cat': 2}, 'c': {'cow': 1}})
    {'a': {'dog': 7, 'cat': 3, 'rat': 8}, 'b': {'dog': 6}, 'c': {'cat': 1, 'cow': 1}, 'd': {'cat': 2}}
    
    >>> combine_grams({'a': {'b': 3, 'c': 9}, 'b': {'a': 10}}, {'a': {'b': 3, 'c': 9}, 'b': {'a': 10}})
    {'a': {'b': 6, 'c': 18}, 'b': {'a': 20}}
    
    >>> combine_grams({'a': {'b': 6, 'c': 18}, 'b': {'a': 20}}, {'a': {'b': 3, 'c': 9}, 'b': {'a': 10}})
    {'a': {'b': 9, 'c': 27}, 'b': {'a': 30}}
    
    '''
    combined_dict = {}
    for k_gram in grams1:
        
# if k-gram in common in grams1 and grams2
        if k_gram in grams2: 
            sub_dict = {} # resets the sub_dict
            for char in grams1[k_gram]: # for each character key in the inner dictionary of grams1[k_gram]
                
# For characters in common for a specific k-gram
                if char in grams2[k_gram]: # if char is in both inner dictionaries of grams1[k_gram] and grams2[k_gram]
                    sub_dict[char] = grams1[k_gram][char] + grams2[k_gram][char] # add the values paired to character key to sub_dict
                    
# For characters unique to grams1 for k-grams in common
                else: 
                    sub_dict[char] = grams1[k_gram][char] # adds item unique to grams1[k_gram] to sub_dict
                    
# For characters unique to grams2 for k-grams in common                    
            for char in grams2[k_gram]: # for each character key in the inner dictionary of grams2[k_gram] 
                if char not in sub_dict: # if the character is unique to grams2[k_gram]
                    sub_dict[char] = grams2[k_gram][char] # add the item unique to grams2[k_gram] to sub_dict

            combined_dict[k_gram] = sub_dict # adds the sub_dict as a value to the k-gram in combined_dict
 
# For k-grams unique to grams1
        else:
            combined_dict[k_gram] = grams1[k_gram] # adds k-grams unique to grams1 to combined_dict
            
# For k-grams unique to grams2            
    for k_gram in grams2:
        if k_gram not in combined_dict:
            combined_dict[k_gram] = grams2[k_gram] # adds k-grams unique to grams2 to combined_dict
            
    return combined_dict

def get_grams_from_files(filenames, k):
    ''' (list, int) -> dict
    It will read in the files at the given filenames, and create a k-grams dictionary of order k for each file. It will combine all
    such k-grams dictionaries and return the combined dictionary.
    
    >>> grams = get_grams_from_files(['raven.txt'], 4)
    >>> len(grams)
    3023
    >>> grams['drea']
    {'r': 1, 'm': 4}
    
    >>> grams = get_grams_from_files(['raven.txt', 'raven.txt'], 4)
    >>> len(grams)
    3023
    >>> grams['drea']
    {'r': 2, 'm': 8}
    
    >>> grams = get_grams_from_files(['raven.txt', 'raven.txt', 'raven.txt'], 4)
    >>> len(grams)
    3023
    >>> grams['drea']
    {'r': 3, 'm': 12}
    
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> len(grams)
    71704
    >>> grams[' rave']
    {'n': 4}
    '''
    dict_list = []
    combined_dict = {}
    for file in filenames:
        fobj = open(file, 'r', encoding = 'utf-8')
        text = fobj.read() 
        k_gram_dict = get_grams(text, k) # gets dictionary of k-grams, using input text
        dict_list.append(k_gram_dict) # appends the dictionary to dict_list
        fobj.close()
    
    if len(dict_list) == 1: # if there is only one dictionary
        return dict_list[0] # return the dictionary itself
        
    for i in range(len(dict_list) - 1): # combine dictionaries n-1 times (ex: n=3 dict, combine (0,1), then combine ((0,1),2))
        combined_dict = combine_grams(dict_list[0], dict_list[1]) # combine the first and second dict in dict_list
        dict_list[0:2] = [combined_dict] # combined_dict takes the spot at dict_list[0]
   
    return combined_dict

def generate_next_char(grams, cur_gram):
    ''' (dict, str) -> str
    Returns the prediction of the next character to follow the k-gram cur_gram, given the dictionary of k-grams grams.
    
    >>> random.seed(9001)
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'a')
    'b'
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'a')
    'c'
    
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'ab')
    Traceback (most recent call last):
    AssertionError: The k-gram input is not in the dictionary grams.
    
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'd')
    Traceback (most recent call last):
    AssertionError: The k-gram input is not in the dictionary grams.
    
    >>> random.seed(1337)
    >>> grams = get_grams_from_files(['raven.txt'], 4)
    >>> generate_next_char(grams, 'drea')
    'm'
    '''
    list_of_char = []
    weights = []
    
    if cur_gram not in grams: # if cur_gram is not in grams, includes cur_gram having different nb of characters than k-grams in grams
        raise AssertionError("The k-gram input is not in the dictionary grams.")
    
    for k_gram in grams:
        
        if k_gram == cur_gram:
            occurrences = 0
            for char in grams[cur_gram]: # for each key in the inner dictionary at grams[cur_gram]
                list_of_char.append(char) # append the key (next possible character) to list_of_char
                occurrences += grams[cur_gram][char] # counts the total nb of occurrences of following characters
                
            for char in grams[cur_gram]:
                weight = grams[cur_gram][char] / occurrences # calculates weight of each character
                weights.append(weight) # appends weight to list weights
                
            break # stops the loop because we found cur_gram already
        
    return random.choices(list_of_char, weights)[0] # returns the prediction as a string

def find_last(text, substr):
    ''' (str, str) -> int
    Returns the index of the last substring in string text which is equal to substr.
    
    >>> find_last('abracadabra', 'a')
    10
    
    >>> find_last('abracadabra', 'ab')
    7
    
    >>> find_last('xoxoxoxoxxoxo', 'xox')
    9
    
    >>> find_last('zimbaba', 's')
    -1
    '''
    common_list = []
    for i in range(len(text)):
        if text[i:i+len(substr)] == substr: # if a substring corresponds to substr in text
            common_list.append(i) # append the index of the first character of that substring
            
    if common_list == []: # if substr is not in text
        return -1 
    
    return common_list[-1] # returns the last index in common_list

def generate_text(grams, start_gram, k, n):
    ''' (dict, str, int, int) -> str
    Generates a piece of text of length n, given the k-grams dictionary grams, the positive integer k, and the starting k-gram
    start_gram. Then cuts off the text at the last empty whitespace or newline character and returns the text.
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> text = generate_text(grams, "Once upon", 5, 200)
    >>> print(text)
    Once upon the tempest tossed this desert land enchanted—tell me—tell me, I implore—
               Quoth the Raven, thou,” I cried, “thy God we both adore—
    Tell the floor.
    “’Tis soul with my head at ease
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> text = generate_text(grams, "Once", 5, 200)
    Traceback (most recent call last):
    AssertionError: The k-gram input is not in the dictionary grams.
    
    >>> random.seed(12)
    >>> grams = get_grams_from_files(['raven.txt'], 4)
    >>> text = generate_text(grams, "Once upon", 7, 200)
    Traceback (most recent call last):
    AssertionError: The k-gram input is not in the dictionary grams.
    
    >>> random.seed(12)
    >>> grams = get_grams("She sells sea shells by the sea shore.", 1)
    >>> generate_text(grams, "S", 1, 20)
    'Shea se by s s shea'
    
    >>> random.seed(12)
    >>> grams = get_grams("housemoneychickendinney", 2)
    >>> generate_text(grams, "mo", 2, 20)
    'moneychickendinneych'
    
    >>> random.seed(13)
    >>> grams = get_grams("house moneychickendinney", 2)
    >>> generate_text(grams, "ho", 2, 20)
    'house'
    '''
    
    if len(start_gram) > k: # if start_gram is longer than k characters
        start_gram = start_gram[0:k] # uses only first k characters
        
    if len(start_gram) > n: # if start_gram has more characters than max length
        start_gram = start_gram[0:n] # uses only first n characters
    
    text = start_gram    
    while len(text) < n:
        text += generate_next_char(grams, start_gram) # generate next char according to previous k-gram
        start_gram = text[len(text)-k:] # update start_gram to become last k characters of text
    
    cut_off_space = find_last(text, ' ') # finds index of last whitespace in text
    cut_off_newline = find_last(text, '\n') # finds index of last newline in text
    

    if cut_off_space > cut_off_newline: # if the index of the last whitespace is after the index of the last newline
        text = text[:cut_off_space] # cut off the text at the last whitespace
    elif cut_off_space < cut_off_newline: # if the index of the last newline is after the index of the last whitespace
        text = text[:cut_off_newline] # cut off the text at the last newline
        
    # if there is neither whitespace nor newline in text, text will not be modified, since cut_off_space and cut_off_newline will be equal
    # if only one of whitespace and newline is present in text, it will work because find_last returns -1 if there is none (comparable)
    
    return text

def repair_text(corrupted_text, error_char, grams, k):
    ''' (str, str, dict, int) -> str
    Given a dictionary of k-grams grams and integer k, replaces all occurences of character error_char in string corrupted_text
    by using the predictions of the Markov model. The repaired string will then be returned.
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> repair_text('it was th~ bes~ of tim~s, i~ was ~he wo~st of~times', '~', grams, 5)
    'it was the best of times, in was Bhe wolst of times'
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> repair_text('i~ was th~ bes~ of tim~s, i~ was ~he wo~st of~times', '~', grams, 5)
    'i~ was the best of times, in was Bhe wolst of times'
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 4)
    >>> repair_text('it was th~ bes~ of tim~s, i~ was ~he wo~st of~times', '~', grams, 5)
    'it was th~ bes~ of tim~s, i~ was ~he wo~st of~times'
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> repair_text('it ~a~ th~ ~es~ of tim~s, i~ was ~he wors~~ of~times', '~', grams, 5)
    'it ~a~ th~ ~es~ of times, is was Ohe worse  of~times'
    '''
    index_list = []
    for index, char in enumerate(corrupted_text):
        if char == error_char:
            index_list.append(index) # generates a list of the indices of the error_char in corrupted_text
            
    repaired_text = ''
    for index, char in enumerate(corrupted_text):
        if index in index_list: # if char at index is an error_char
            if index < k or repaired_text[index-k:index] not in grams: # if there is no k-gram before the error_char
                repaired_text += char # add error_char to string
            elif repaired_text[index-k:index] in grams: # if a k-gram exists before the error_char
                repaired_text += generate_next_char(grams, repaired_text[index-k:index]) # add prediction of k-gram    
        else:
            repaired_text += char # if char is not an error_char
        
    return repaired_text
                    
if __name__ == '__main__':
    doctest.testmod()

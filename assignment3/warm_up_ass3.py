import doctest
import math

def same_elements(my_list):
    ''' (list) -> bool
    Returns true if all the elements in each sublist are the same, false otherwise.
    >>> same_elements([[1, 1, 1], ['a', 'a'], [6]])
    True
    >>> same_elements([[1, 6, 1], [6, 6]])
    False
    '''
    for sublist in my_list:
        same = sublist[0]   # first element of sublist
        for ele in sublist:
            if ele != same:
                return False
    return True
    
    
def flatten_list(my_list):
    ''' (list) -> list
    Returns a one-dimensional list containing all the elements of the sublists in my_list.
    >>> flatten_list([[1, 2], [3], ['a', 'b', 'c']])
    [1, 2, 3, 'a', 'b', 'c']
    >>> flatten_list([[]])
    []
    '''
    new_list = []
    for sublist in my_list:
        for ele in sublist:
            new_list.append(ele)

    return new_list

def get_most_valuable_key(my_dict):
    ''' (dict) -> str
    Returns the key mapped to the largest value in d.
    >>> get_most_valuable_key({'a' : 3, 'b' : 6, 'g' : 0, 'q' : 9})
    'q'
    >>> get_most_valuable_key({'Bob' : 20, 'Sam' : 17, 'Raf' : 21})
    'Raf'
    '''
    largest_int = -math.inf #smallest nb, so first int is always first largest int
    for key in my_dict:
        if my_dict[key]> largest_int:
            largest_int = my_dict[key]
            valuable_key = key
    return valuable_key

def add_dicts(dict1, dict2):
    ''' (dict, dict) -> dict
    Returns a dictionary which is the result of merging the two input dictionary that is if a key is in
    both dictionaries then add the two values.
    >>> d1 = {'a':5, 'b':2, 'd':-1}
    >>> d2 = {'a':7, 'b':1, 'c':5}
    >>> add_dicts(d1, d2) == {'a': 12, 'b': 3, 'c': 5, 'd': -1}
    True
    
    >>> d1 = {'a':5, 'b':2, 'd':-1, 'f':1}
    >>> d2 = {'a':7, 'b':1, 'c':5, 'g':5}
    >>> add_dicts(d1, d2)
    {'a': 12, 'b': 3, 'c': 5, 'd': -1, 'f': 1, 'g': 5}
    '''
    added_dict = {}
    unique_keys = []
    for key1 in dict1:
        if key1 in dict2: # if key in both dictionaries
            added_dict[key1] = dict1[key1] + dict2[key1] # add the values paired with the key
        else:
            unique_keys.append(key1) # append keys from dict1 to unique_keys
            
    for key2 in dict2:
        if key2 not in added_dict:
            unique_keys.append(key2) # append keys from dict2 to unique_keys
            
    unique_keys.sort() # sort the keys in alphabetical order
            
    for key in unique_keys:
        if dict1.get(key) != None:
            added_dict[key] = dict1.get(key) # if the key belongs to dict1, add to added_dict
        else:
            added_dict[key] = dict2.get(key) # if the key belongs to dict2, add to added_dict
    return added_dict

def reverse_dict(d):
    ''' (dict) -> dict
    Returns a dictionary where the values in d are now keys mapping to a list containing all the keys in d which mapped to them.
    >>> a = reverse_dict({'a': 3, 'b': 2, 'c': 3, 'd': 5, 'e': 2, 'f': 3})
    >>> a == {3 : ['a', 'c', 'f'], 2 : ['b', 'e'], 5 : ['d']}
    True
    '''
    reverse_dict = {}
    
    for key in d:
        if d[key] in reverse_dict:
            reverse_dict[d[key]].append(key)   
        else:
            reverse_dict[d[key]] = [key]
            
    return reverse_dict
         
if __name__ == "__main__":
    doctest.testmod()
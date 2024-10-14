# Author: Shawn Yat Sin
# ID: 261052225
# Question 1: Follow the trail in a treasure map, split across multiple files.

import doctest

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
VALID_CHARS = ['>', '<', '^', 'v', '.', '*', '|', 'X', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

def is_matrix(m):
    """ (list) -> bool
    Returns true if the list m is a matrix, such that each inner list has the same length.

    >>> a = [[19, 8, 23, 11], [25, 22, 30, 26], [23, 20, 29, 16]]
    >>> is_matrix(a)
    True
    
    >>> b = [[1, 2, 3], [2, 3], [4, 5, 6]]
    >>> is_matrix(b)
    False
    
    >>> c = []
    >>> is_matrix(c)
    True
    """
    if len(m) == 0:
        return True
    
    size = len(m[0])
    for s in m:
        if len(s) != size:
            return False
        
    return True

def load_treasure_map(filename):
    ''' (str) -> list
    Opens a treasure map at the filename and loads the treasure map into a list of lists. Returns the list.
    Raises an AssertionError if there is an issue with the format of the file.
    
    >>> load_treasure_map('map0.txt')
    [['>', '>', '>', 'v', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'v', '.', '.', '.', '<', '<', '.'], ['.', '.', '.', 'v', '.', '.', '.', '.', '.', '.'], ['v', '.', '.', 'v', '.', '.', '.', '.', '^', '.'], ['v', '.', '.', '>', '>', '*', '.', '.', '^', '.'], ['v', '.', '.', '.', '.', '.', '.', '.', '^', '.']]
    
    >>> load_treasure_map('map1.txt')
    [['.', '>', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '<', '<', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '>', 'v', '.', '.', '.'], ['.', '^', '.', '.', '.', '^', 'v', '.', '.', '.'], ['.', '^', '.', '.', '.', '.', '>', '>', '8', '.']]
    
    >>> load_treasure_map('not_a_matrix.txt')
    Traceback (most recent call last):
    AssertionError: The treasure map contained in not_a_matrix.txt is not a matrix.
    
    >>> load_treasure_map('map4.txt')
    Traceback (most recent call last):
    AssertionError: The treasure map contained in map4.txt has an invalid character.
    '''
    map_as_lists = []
    fobj = open(filename, 'r') # open file at filename
    treasure_map = fobj.read() # read file and return string of characters
    for char in treasure_map:
        if char not in VALID_CHARS: # checks for invalid characters
            raise AssertionError('The treasure map contained in ' + filename + ' has an invalid character.')
        
    treasure_map_list = treasure_map.split() # returns a list of substrings corresponding to a line in file
    if not is_matrix(treasure_map_list): # checks if the treasure_map_list is a matrix
        raise AssertionError('The treasure map contained in ' + filename + ' is not a matrix.')
    
    for line in treasure_map_list:
        map_as_lists.append(list(line)) # appends each substring as a list to map_as_lists
        
    fobj.close() # closes the file
    
    return map_as_lists

def write_treasure_map(treasure_map, filename):
    ''' (list, str) -> NoneType
    Writes the characters in list treasure_map to a file at filename, with a new line after each row in treasure_map.
    
    >>> my_map = load_treasure_map('map0.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True
   
    >>> my_map3 = load_treasure_map('map8.txt')
    >>> write_treasure_map(my_map3, 'new_map.txt')
    >>> my_map4 = load_treasure_map('new_map.txt')
    >>> my_map3 == my_map4
    True
    
    >>> my_map = load_treasure_map('map1.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('map0.txt')
    >>> my_map == my_map2
    False
    '''
    fobj = open(filename, 'w')
    for line in treasure_map: # for sublist in list treasure_map
        for char in line: # for string char in sublist
            fobj.write(char) # write char to fobj 
        fobj.write('\n') # skip a line after last character in sublist is written
    
    fobj.close()

def write_X_to_map(filename, row, col):
    '''(str, int, int) ->  NoneType
    Reads in the map at the given filename, inserts an X into the given row and column position, then saves the map to a new file
    with 'new_' prepended to the given filename.
    
    >>> write_X_to_map('map8.txt', 3, 6)
    >>> map = load_treasure_map('new_map8.txt')
    >>> print(map[3])
    ['.', '.', '>', '>', '>', '>', 'X', '.', '.', '.']
        
    >>> write_X_to_map('map0.txt', 0, 0)
    >>> map = load_treasure_map('new_map0.txt')
    >>> print(map[0])
    ['X', '>', '>', 'v', '.', '.', '.', '.', '.', '.']
    
    >>> write_X_to_map('map0.txt', 10, 11)
    Traceback (most recent call last):
    AssertionError: The position input by row and col does not exist in the map.
    '''
    og_map = load_treasure_map(filename) # convert treasure map in the file to a list of lists
    if row >= len(og_map) or col >= len(og_map[0]): # checks if the position of X is on the map
        raise AssertionError("The position input by row and col does not exist in the map.")
    
    og_map[row][col] = 'X' # inserts X into valid position
    write_treasure_map(og_map, 'new_'+filename) # writes og_map with X inserted to a new file with 'new'_ prepended to the filename

def follow_trail(filename, treasure_map, start_row, start_col):
    ''' (str, list, int, int) -> tuple
    Follows the trail in the given treasure_map, starting at treasure_map[start_row][start_col]. Performs appropriate action according to
    the character of the trail. Returns a tuple of three elements defined by the character of the trail.
    
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map0.txt', my_map, 0, 0)
    (1, 4, 5)
    
    >>> my_map = load_treasure_map('map1.txt')
    >>> follow_trail('map1.txt', my_map, 4, 5)
    (8, 0, 0)
    
    >>> my_map = load_treasure_map('map8.txt')
    >>> follow_trail('map8.txt', my_map, 0, 0)
    (-1, 3, 6)
    
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map0.txt', my_map, 3, 0)
    Traceback (most recent call last):
    AssertionError: The current position is outside of the map.
    
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map0.txt', my_map, 11,11)
    Traceback (most recent call last):
    AssertionError: The starting position does not exist on the map.
    
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map00.txt', my_map, 0, 0)
    Traceback (most recent call last):
    AssertionError: The filename does not correspond to a valid map file.
    
    >>> my_map = load_treasure_map('map9.txt')
    >>> follow_trail('map9.txt', my_map, 4, 8)
    Traceback (most recent call last):
    AssertionError: The trail is leading you in circles.
    
    >>> my_map = load_treasure_map('map9.txt')
    >>> follow_trail('map9.txt', my_map, 0, 0)
    Traceback (most recent call last):
    AssertionError: The trail has reached a dead end.
    '''
    if filename[0:3] != 'map' or filename[3] not in DIGITS or filename[4:] != '.txt':
        raise AssertionError("The filename does not correspond to a valid map file.")
    
    if start_row >= len(treasure_map) or start_col >= len(treasure_map[0]): # if the starting position is not within the grid
        raise AssertionError("The starting position does not exist on the map.")
    
    map_nb = int(filename[3]) # records map number
    position = treasure_map[start_row][start_col] # starting position
    current_row = start_row
    current_col = start_col
    moves = [] # keeps track of the moves taken
    
    while position != '.':
        if position in ['>', '<', 'v', '^']: # if the character is an arrow
            if position == '>':
                current_col += 1
            elif position == '<':
                current_col -= 1
            elif position == 'v':
                current_row += 1
            elif position == '^':
                current_row -= 1
        
        if current_row == len(treasure_map) or current_col == len(treasure_map[0]): # if arrow points outside map to the right or down
            raise AssertionError("The current position is outside of the map.")
        
        if current_row < 0 or current_col < 0: # if arrow points outside map to the left or up
            raise AssertionError("The current position is outside of the map.")
        
        elif position == '*':
            map_nb += 1
            if map_nb == 10: # in the case where the map9.txt file trail ends on '*'
                raise AssertionError("The trail has reached a dead end.") # prevents map num from being 10
            return (map_nb, current_row, current_col)

        elif position == '|':
            map_nb -= 1
            if map_nb == -1: # in the case where the map0.txt file trail ends on '|'
                raise AssertionError("The trail has reached a dead end.") # prevents map num from being -1 
            return (map_nb, current_row, current_col)
        
        elif position in DIGITS: # if position is a digit
            return (int(position), 0, 0)
        
        elif (current_row, current_col) in moves: # if the trail's next position has already been checked
            raise AssertionError("The trail is leading you in circles.") # it will cause an infinite loop otherwise
        
        position = treasure_map[current_row][current_col] # updates the position
        moves.append((current_row, current_col)) # appends the coordinates of the position to moves
        
    if position == '.':
        write_X_to_map(filename, current_row, current_col) # inserts an X at the coordinates and saves the map to a new file
        return (-1, current_row, current_col)
    
def find_treasure(start_map_num):
    ''' (int) -> tuple
    Loads the corresponding map file, and starts following the trail at position 0, 0 of that file. Continues
    following the trail through other map files as needed. Places an 'X' at the conclusion of the trail and
    saves the updated treasure map to a new file with 'new_' prepended to the current map filename.
    Returns a tuple of the row and column index where the 'X' was placed in that file.
    >>> find_treasure(0)
    (3, 6)
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    
    >>> find_treasure(8)
    (3, 6)
    
    >>> find_treasure(1)
    (0, 0)
    
    >>> find_treasure(9)
    Traceback (most recent call last):
    AssertionError: The trail has reached a dead end.
    '''
    filename = 'map' + str(start_map_num) + '.txt' # obtain map file with corresponding map number
    treasure_map = load_treasure_map(filename) # convert treasure map in the file to a list of lists
    next_step = follow_trail(filename, treasure_map, 0, 0) # tuple with map_nb and coordinates
    map_nb = next_step[0]
     
    while map_nb != -1: # while treasure not found
        filename = 'map' + str(map_nb) + '.txt' # update filename
        treasure_map = load_treasure_map(filename) # update treasure map
        next_step = follow_trail(filename, treasure_map, next_step[1], next_step[2]) # update tuple
        map_nb = next_step[0] # update map_nb
            
    return (next_step[1], next_step[2]) # returns row and column of treasure


    
if __name__ == "__main__":
    doctest.testmod()
    
    
write_X_to_map('map8.txt', 3, 6)
    
# Author: Shawn Yat Sin
# ID: 261052225

# Here are the rules to translate a single English word into Pig Latin:

# Step 1:
# If a word starts with one or more consonants, the consonant(s) are moved at the end of the
# word. So, for instance, ‘pig’ becomes ‘igp’, and ‘strong’ becomes ‘ongstr’.
# If a word starts with a vowel, a ‘w’ is added at the end of the word. So, for instance, ‘english’
# becomes ‘englishw’.

# Step 2:
# Add the suffix ‘ay’ to the result of the first step. So, for instance, ‘igp’ becomes ‘igpay’,
# ‘ongstr’ becomes ‘ongstray’, and ‘englishw’ becomes ‘englishway’.

def pig_latin_word_to_english(pig_latin_word):
    ''' (str) -> str
    Returns pig_latin_word as a string translated into English.
    
    >>> pig_latin_word_to_english('igPay,') # can add comma
    'Pig,'
    
    >>> pig_latin_word_to_english('Strong') # returns original string if not in Pig Latin
    'Strong'
    
    >>> pig_latin_word_to_english('englishway, igPay') # does not accept two words
    ''
    
    >>> pig_latin_word_to_english('Englishway!')
    'English!'
    
    >>> pig_latin_word_to_english('ongStray!!')
    'Strong!!'
    
    >>> pig_latin_word_to_english('urrayHay!') # for multiple 'ay'
    'Hurray!'
    
    '''
# 1. Create reference lists for letters
    consonant_lower = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    consonant_upper = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    consonant_list = consonant_upper + consonant_lower
    vowel_lower = ['a','e','i','o','u','y']
    vowel_upper = ['A','E','I','O','U','Y']
    vowel_list = vowel_lower + vowel_upper
    letters = consonant_list + vowel_list
    minus_ay = pig_latin_word
    shift = 0
    
# 2. Return empty string for invalid inputs (empty or more than one word)
    for i in range(len(pig_latin_word)):
        if pig_latin_word[i] in ['', ' ', '-']: # if there is more than one word or the string is empty
            return ''
        
# 3. Remove 'ay' from Pig Latin word

# 3.1 Remove 'ay' from simple Pig Latin words             
        if pig_latin_word[i:i+2] == 'ay' and i == len(pig_latin_word) - 2: # if the word has 'ay' as the two last characters and has no symbols at the end
            minus_ay = minus_ay[:i] # [beg: 'ay']

# 3.2 Remove 'ay' from word with symbols at the end
        if pig_latin_word[i] not in letters: # for words with symbols at the end 
            while pig_latin_word[i + shift] not in letters: # checks number of symbols at the end of word
                if pig_latin_word[i+ shift] in ['', ' ', '-']: # in case symbol in middle before invalid shows up, ex: ('englishway, igPay')
                    return ''
                shift += 1
                if i + shift == len(pig_latin_word): # to avoid IndexError
                    break
                
# 3.21 Check if word without the symbols is in Pig Latin, and removes 'ay' if True               
            if pig_latin_word[i-2:i] == 'ay' and i-2 == len(pig_latin_word) - 2 - shift: # if the word is in Pig Latin despite symbols
                minus_ay = minus_ay[:i-2] + minus_ay[i:] # add string from beginning until 'ay' + symbols at the end
                break # to not count any other non-letters
            
            else: # if word has symbols and is not in Pig Latin
                return pig_latin_word
            
# 4. Return original word if not in Pig Latin (optional)             
    if minus_ay == pig_latin_word: # if the word is not in Pig Latin (meaning minus_ay has not been updated)
        return pig_latin_word
    
# Next step: translate the word into English
    
# 5. For situations with symbols at the end                         
    counter = 0
    eng_word = minus_ay

# 5.1 Update the counter to take into account symbols 
    if minus_ay[-1] not in letters: # for symbols at the end of the word
        for i in range(shift): # updates the counter for the nb of symbols
            counter += 1
            
# 5.2 Transform word that ends with 'w' to English and return it            
        if minus_ay[-1 - counter] == 'w': # for words that start with vowel
            eng_word = minus_ay[:len(minus_ay)- 1 - counter] + minus_ay[len(minus_ay) - counter:] # [:'w'] + symbols ex: englishw!
            return eng_word

# 5.3 Transform word that ends with consonants to English and return it
        while minus_ay[-1 - counter] in consonant_list: # while the last letter before the symbol is a consonant
            eng_word = minus_ay[len(minus_ay) - 1 - counter] + eng_word[:len(minus_ay) - 1 - shift] + eng_word[len(minus_ay) - shift:]
            # last letter + [beg:last letter] + symbols
            # counter vs shift: counter updates for the string minus_ay, while eng_word updates for the shift
        
            if minus_ay[-1 - counter].isupper(): # capital letter allows while loop to know when to stop  ex: 'ongstray!!' == 'ngstro!!'
                break
            counter += 1
            
# 6. Transform word that ends with 'w' to English and return it    
    elif minus_ay[-1] == 'w': 
        eng_word = minus_ay[:len(minus_ay)-1] # [:'w']
        
# 7. Transform word that ends with consonants to English and return it    
    else: 
        while minus_ay[-1 - counter] in consonant_list:
            eng_word = minus_ay[len(minus_ay) - 1 - counter] + eng_word[:len(minus_ay) - 1]
        
            if minus_ay[-1 - counter].isupper():
                break
            counter += 1
         
    return eng_word # after if, elif or else statements


def pig_latin_phrase_to_english(pig_latin_phrase):
    ''' (str) -> str
    Returns pig_latin_phrase as a string translated into English.
    
    >>> pig_latin_phrase_to_english('atchWay Outway! eyThay Areway omingCay orFay Youway extNay')
    'Watch Out! They Are Coming For You Next'
    
    >>> pig_latin_phrase_to_english('Iway ishWay hisTay asWay Easyway! LMAO!!!')
    'I Wish This Was Easy! LMAO!!!'
    
    >>> pig_latin_phrase_to_english('odayTay isway away eatGray ayDay oTay earnLay oreMay aboutway ythonPay')
    'Today is a Great Day To Learn More about Python'
    
    >>> pig_latin_phrase_to_english('Yesterdayway, Iway awSay away oneDray ealStay yMay abyBay! :(')
    'Yesterday, I Saw a Drone Steal My Baby! :('
    
    '''
# 1. Count the number of words in a phrase
    index_spaces = [] # takes the indexes of the spaces in the string pig_latin_phrase
    nb_spaces = 0
    for i in range(len(pig_latin_phrase)): 
        if pig_latin_phrase[i] == ' ':
            index_spaces.append(i)   # adds the index of the space into index_spaces
            nb_spaces += 1 # counts the number of spaces
            
    nb_words = nb_spaces + 1
    
# 2. Translate words individually and add them to a new string translation     
    translation = ''
    counter = 0
    
    while counter < nb_words:
        
# 2.1 Translate the first word and add it to translation
        if counter == 0: 
            word_translated = pig_latin_word_to_english(pig_latin_phrase[:index_spaces[0]]) # [: first space]
            translation += word_translated
            counter += 1
            
# 2.2 Translate words after first word and add them to translation            
        else:   
            if counter > 0 and counter < nb_words - 1: # for any word in between first and last 
                word_translated = pig_latin_word_to_english(pig_latin_phrase[index_spaces[counter-1]+1:index_spaces[counter]]) 
                # [previous space + 1: current space]
                
            elif counter == nb_words - 1: # for last word
                word_translated = pig_latin_word_to_english(pig_latin_phrase[index_spaces[counter - 1] + 1:])
                # [before last space + 1:]
                
            translation += ' ' + word_translated # adds a space + the word_translated to translation
            counter += 1
            
    return translation           
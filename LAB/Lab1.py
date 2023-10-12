#Checks if length is 26
#Then checks if character is capital/lower case letter in alphabet
#If so, checks if is the only instance of that letter (capital or lower)
#If all conditions are met, string is determined valid
def isValid(txt): #DHANKKKKK
    '''
        >>> isValid('qwertyuiopASDFGHJKLzxcvbnm')
        True
        >>> isValid('hello there, fall is here!')
        False
        >>> isValid('123456yh')
        False
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBMn')
        True
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBnn')
        False
        >>> isValid('12aaaaaaaaaaa6543212345678')
        False
    '''
    # - YOUR CODE STARTS HERE -
    #Takes a string a_string and returns True if a_string is a string that has exactly 26 characters and each  of  the  letters  'a'/'A'  -'z'  /'Z'  appeared  only  once.
    isStr = True
    if(len(txt)!=26):
        isStr = False
    else:
        for l in txt:
            if(txt.count(l) == 1):
                if(ord(l) >= ord('a') and ord(l) <= ord('z')):
                    if(txt.count(l.upper()) != 0):
                        isStr = False
                elif ord(l) >= ord('A') and ord(l) <= ord('Z'):
                    if(txt.count(l.lower()) != 0):
                        isStr = False
            else:
                isStr = False 
    return isStr
        
    pass
#Appends line of file to list with white spaces stripped
def get_words(filename):
    '''
        Complete the current implementation to work as directed in the handout. No more than 3 lines are required
        .txt file for this doctest is available on Canvas and must be saved in the 
        same directory as your .py file
        >>> get_words('contents.txt')
        ['week', 'bat', 'aquatic', 'eggs', 'threatening', 'crash', 'educated', 'adjoining', 'bent', 'mice', 'belief', 'adjustment', 'blood', 'smooth', 'kaput', 'mountain', 'digestion', 'enchanted', 'wandering', 'fresh']
        >>> len(get_words('contents.txt'))
        20
    '''
    output = []
    with open(filename) as text: # Open, read and close file
        for line in text:        # text contains the entire content of the .txt file   
    # - YOUR CODE STARTS HERE -
            output.append(line.strip())
    return output
    pass
#Iterates through each word in list
#Assigns length of word to key
#Iterates through words again (nested loop) and checks if there are any other words with same length (same key)
#If so, adds to value
def get_histogram(words):
    '''
        >>> get_histogram(['hello', 'there', 'spring', 'is', 'here'])
        {5: 2, 6: 1, 2: 1, 4: 1}
        >>> list_of_words = get_words('contents.txt')
        >>> get_histogram(list_of_words)
        {4: 4, 3: 1, 7: 1, 11: 1, 5: 4, 8: 2, 9: 4, 6: 2, 10: 1}
    '''
    # - YOUR CODE STARTS HERE -
    hist = {}
    for i in words:
        value = 0
        key = len(i)
        for j in words:
            if(len(j)==key):
                value+=1
        hist[key] = value
    return hist
    pass
#Creates empy string fString
#Iterates through input (aString) and if character is not in alphabet, appends white space
#Else appends character
#Appends non-characters to list
#Iterates through list and assigns element to key and value is number of times element appears in list
def removePunctuation(aString):
    '''
        >>> removePunctuation("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        >>> data = removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    '''
    # - YOUR CODE STARTS HERE -
    punct = {}
    lst = []
    fString = ""
    for l in aString:
        if l.isalpha() == False and l!= ' ':
            fString += " "
            lst.append(l)
        else:
            fString += l
    for i in lst:
        punct[i] = lst.count(i)
    return fString, punct
    pass
if __name__ == "__main__":
    import doctest
    #doctest.run_docstring_examples(removePunctuation, globals(), name='Lab1',verbose=True) # Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run

    #doctest.testmod() # Uncomment this line if you want to run the docstring in all functions


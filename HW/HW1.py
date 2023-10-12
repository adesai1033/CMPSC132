# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

#Finds factors for width and height
#Starts from 1, to area
#Width increases by 1 height becomes area/width
#Checks if width height pair result in correct perimeter
#If so, checks if height is integer by seeing if area is correct when converted to integer
#Iterates until width is area

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    
    width = 1
    height = area
    for width in range(area):
        if(2*width + 2*height == perimeter):
            if((int)(width) * (int)(height) == area):
               if(width>height):
                   return (int)(width)   
               else:
                   return (int)(height)
        else:
            width += 1
            height = area/width
            
    return False   
    pass



#Iterates through input creates a temporary list of values
#Iterates through input again
#If count of values is 1, appends to inversed dictionary 
def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    #- YOUR CODE STARTS HERE
    tempVals = []
    invDict = {}
    for key in d:
        tempVals.append(d[key])
    for key in d:
        if(tempVals.count(d[key]) == 1):
           invDict[d[key]] = key
    return invDict
    pass




#Creates a list with each element being a word or punctuation mark from the file
#Then iterates through list and uses nested loops to find all elements right after each element (including repeats)
#Appends this to temp
#Finally iterates through words and appends elements from temp list to another temp list to ensure order corresponds correctly
#appends to dictionary where key is some element from words list and value is a list of all elements found right after said key
def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """

    with open(file) as f: 
        contents = f.read()
    

    #- YOUR CODE STARTS HERE
    words = []
    element = ""
    dct = {}
    temp = []
    for char in "." + contents.replace('\n',""):
        if(char.isalnum() == False and char!=' '):
            if(element!=""):
                words.append(element)
            words.append(char)
            element = ""
        elif char.isalnum() == True:
            element += char
        elif char == ' ':
            words.append(element)
            element = ""
    for i in range(0,len(words)-1):
        temp = []
        temp.append(words[i+1])
        for j in range(0,len(words)):
            if(words[i] == words[j] and j!= len(words)-1):
                if(temp.count(words[j+1])==0):
                    temp.append(words[j+1])
        temp2 = []
        for k in range(len(words)):
            if(temp.count(words[k]) == 1):
                if(temp2.count(words[k]) == 0):
                    temp2.append(words[k])
        dct[words[i]] = temp2         
    return dct
        
        
#Loops until modulus operation results in original number
#Starts at position 1 each time loop iterates position increases
#If digit is found, returns position
#Otherwise multiplies divisor by 10
def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
        >>> getPosition(5,5)
        1
    """
    #- YOUR CODE STARTS HERE
    divisor = 1
    pos = 1
    while(num%divisor!=num):
        if((num//divisor)%10 == digit):
            return pos
        pos +=1
        divisor*=10
    return False
    pass


#Appends input to list
#Iterates until last element is 1
#Uses modulus to determine whether number is odd or even
def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    #If odd, *3 + 1
    #If even, /2
    hailstone = [(int)(num)]
    while(hailstone[-1] != 1):
        if(hailstone[-1]%2 == 0):
            hailstone.append((int)(hailstone[-1]/2))
        else:
            hailstone.append((int)(hailstone[-1]*3+1))
    return hailstone
            
    pass

#Iterates until half of input
#Uses modulus to determine largest number with remainder of 0
def largeFactor(num):
    """
        >>> largeFactor(15)
        5
        >>> largeFactor(80)
        40
        >>> largeFactor(13)
        1
    """
    #- YOUR CODE STARTS HERE
    factor = 1
    for i in range(1,int(num/2)+1):
        if(num%i == 0):
            factor = i
        
    return factor 
    pass


if __name__=='__main__':
    import doctest
    #doctest.run_docstring_examples(successors, globals(), name='HW1',verbose=True) # replace rectangle for the function name you want to test
    doctest.testmod() # Uncomment this line if you want to run the docstring in all functions

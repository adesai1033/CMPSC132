# LAB3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    #YOUR CODE STARTS HERE
    tempLst = aList.copy() #Creates copy of list (have to use .copy()) because otherwise changes to tempLst would also effect aList
    if len(aList) == 0: #Base Case
        return 0        #Returns 0 so once this is completed previous calls can 'compile' and add up 

    elif aList[0] == item: #Element was found
        tempLst.pop(0) #Remove first element so you can evaluate next element in next call
        return 1 + get_count(tempLst, item) #Because element was found you return 1 + whatever the next function call yields
                                            
    elif aList[0] != item:
        tempLst.pop(0)  
        return get_count(tempLst, item) #Returns new list (first element popped)


    pass


def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    ## YOUR CODE STARTS HERE
    tempLst = numList.copy() #Creates copy of list
    if len(numList) == 0: #This is base case since we are popping the first element each function call
        return [] 

    elif numList[0] == old:
        
        tempLst.pop(0)
        return [new] + replace(tempLst,old,new) #If the 'old' element is found the 'new' element is returned in its place plus the
                                                #the function call with same parameters except the list being one element shorter (first element popped)
    elif numList[0] != old:     #If the desired element is not found

        temp = numList[0]
        tempLst.pop(0)
        return [temp] + replace(tempLst,old,new)    #Nothing will be changed in the list but we will pop the first element
                                                    #so that we can evaluate the next item in the list
    pass


def cut(aList):
    '''
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -3, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
    '''
    ## YOUR CODE STARTS HERE
    tempLst = aList.copy()      #Creates copy of list
    if len(tempLst) == 0:       #Base case is when all elements have been popped
        return []

    elif tempLst[0] < 0:
        temp = tempLst[0]
        tempLst.pop(0)  #Pops from list so we can get to end of list eventually
        if len(tempLst) > 0 and abs(temp) - 1 >0 and tempLst[0] > 0: #Even tho base case is when list is empty we have to check
            tempLst[0] = (abs(temp) - 1)*-1                          #here as well because we just popped an element
        return cut(tempLst)                                          #If condition causes elements to be removed until the absolute value in the next call is 0
                                                                     #If the absolute value - 1 is more than 0 we want to remove elements abs val - 1 times
                                                                     #So we set the first element in the list to the negative of that value
    else:   #When value >= 0
        temp = tempLst[0] #If the val
        tempLst.pop(0)  #Pops from list so we can get to end of list eventually
        return [temp] + cut(tempLst)    #Returns the element + the function call of the modified list
    pass


def neighbor(n):
    '''
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    '''
    ## YOUR CODE STARTS HERE
    x = n//10 #Each time the function is called the number gets rid of the last digit
    if n == 0: #Base case occurrs when 
        return 0

    elif n%10 != n//10%10:  #Checks if value in last place (1s) is same as neighbor (10s)
        return n%10 + 10* neighbor(x) #If this case is found returns value in ones place + 10 times neighbor call
                                      #Compounds each call 
    else:
        return neighbor(x)            #Returns number with last digit dropped

    pass

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(neighbor, globals(), name='Lab3',verbose=True) 
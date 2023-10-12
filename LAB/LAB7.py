# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # YOUR CODE STARTS HERE
        return self._heap[0] #First item in list will be the minimum value by minHeap property
        pass
    

    def _parent(self,index):
        # YOUR CODE STARTS HERE
        if index>1: #Index must be valid
            return self._heap[index//2-1] #Return parent
        return None
        
        pass

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        if index != 0 and len(self)>2*index-1: #Checks if index is valid
            return self._heap[index*2-1] #Returns child
        return None

        pass


    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        if index != 0 and len(self)>2*(index-1)+1: #Checks if index is valid
            return self._heap[index*2] #Returns child
        return None
        pass
 

    def insert(self,item):
        # YOUR CODE STARTS HERE
        self._heap.append(item) #Adds item to heap
        i = len(self)-1
            
        while (i != 0 and self._parent(i+1) > item) : 
            self._heap[(i-1)//2], self._heap[i] = self._heap[i], self._heap[(i-1)//2] #swap operation until heap property is satisfied
            i = (i-1)//2 #New index of item just appended
        pass
            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted = self._heap[0]
            self._heap=[]
            return deleted
        else:
            deleted = self._heap[0]
            self._heap[0] = self._heap[-1] #Makes right most child root of heap
            self._heap.pop() #Removes last element since it has now been moved to top of the heap
            i = 0
            
            while self._leftChild(i+1) is not None and i<(len(self)-1)//2 : #Checks to make sure left is not None
                left = self._leftChild(i+1) #+1 because 1 indexed
                right = self._rightChild(i+1)
                if right is not None and self._heap[i]> min(left,right): #minimum of left and right
                    if right>left:
                        self._heap[(i+1)*2-1], self._heap[i] = self._heap[i], self._heap[(i+1)*2-1] #swap operation
                        i = (i+1)*2-1 #New index of item we are percolating down
                    else:
                        self._heap[(i+1)*2], self._heap[i] = self._heap[i], self._heap[(i+1)*2] #swap
                        i = (i)*2+1 #new index of item we are percolating down 
                elif right is None and left < self._heap[i]:
                    self._heap[(i+1)*2-1], self._heap[i] = self._heap[i], self._heap[(i+1)*2-1] #swap
                    i = (i+1)*2-1 #new index of item we are percolating down
                    
                else:
                    return deleted
            return deleted

            
            pass



def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    # YOUR CODE STARTS HERE
    minHeap = MinBinaryHeap()
    final = []
    for i in numList:
        minHeap.insert(i)
    while len(minHeap) != 0:
        final.append(minHeap.deleteMin())
    return final


    pass

if __name__=='__main__':
    import doctest
    #doctest.testmod(verbose=True)
    doctest.run_docstring_examples(heapSort, globals(), name='LAB7',verbose=True) 
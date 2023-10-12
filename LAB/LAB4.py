# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList() 
        >>> x.add(4.5) 
        >>> x.add(-3) 
        >>> x.add(0) 
        >>> x.add(5) 
        >>> x.add(2) 
        >>> x.add(-9) 
        >>> x.add(12.7) 
        >>> x.add(-3.5) 
        >>> x.add(2) 
        >>> x.add(4) 
        >>> x.add(1) 
        >>> x.add(3) 
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.replicate()
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -9 -> -3.5 -> -3.5 -> -3 -> -3 -> 0 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4.5 -> 4.5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 12.7 -> 12.7
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.add(0)
        >>> x.add(3)
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> myList=x.replicate()
        >>> myList
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -9 -> -3.5 -> -3.5 -> -3 -> -3 -> 0 -> 0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4.5 -> 4.5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 12.7 -> 12.7
        >>> myList.removeDuplicates()
        >>> myList
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.add(13)
        >>> x.add(13) 
        >>> x
        Head:Node(-9)
        Tail:Node(13)
        List:-9 -> -3.5 -> -3 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4.5 -> 5 -> 12.7 -> 13 -> 13
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-9)
        Tail:Node(13)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7 -> 13
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

    #adds a new Node with value=item to the list making sure that the ascending order is preserved         
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value) #Creates node obj
        current = self.head
        if(self.isEmpty()): #If linked list is empty
            self.head = new_node #Head and tail is new_node
            self.tail = new_node
            return

        elif(current.value >= value): #If the head value is larger than the value
            new_node.next = current #Links new_node to head of list
            self.head = new_node    #And redefines head as new node
            return

        else:
            while current.next is not None: 
                if current.next.value>value: #If the next value is greater than the value of the node
                    new_node.next = current.next #Inserts node before value it is less than
                    current.next = new_node       
                    break #Prevents infinite loop
                current = current.next
            if(current.next is None): #If next value is none
                current.next = new_node #Links node to currents next
                self.tail = new_node #Defines tail as new_node
            
               
                
        return
        pass


    def replicate(self):
        # --- YOUR CODE STARTS HERE
        if self.isEmpty():
            return None

        
        lst = SortedLinkedList() #Creates SortedLinkedList Obj
        current = self.head
        while current:  
            val = current.value
            if isinstance(val, float) == True or val<0: #For non-int values & values<1
                lst.add(val) #Add to the sorted linked list twice
                lst.add(val)
            elif val == 0: #For values of 0
                lst.add(val) #Add only once
            else: #For other values
                for i in range (val):
                    lst.add(val) #Add to the list value number of times
            current = current.next #Iterates
        return lst


        pass


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
     
        
        current = self.head #First value
        while current.next!=None:
            if current.value == current.next.value: #Checks if 1st value is same as 2nd value
                current.next = current.next.next #Links prev to node after its next

                    
            else: #Only further iterates when duplicate is not found
                current = current.next 
                
        return 
        pass

if __name__=='__main__':
    import doctest
    #doctest.testmod()  # OR
    doctest.run_docstring_examples(SortedLinkedList, globals(), name='LAB4',verbose=True) 
